"""The shared fitting routine: equation (3) with cluster-robust errors.

Every estimate in the paper's occurrence analysis comes through `fit`.
Only the exposure under test changes between them, which is what makes
the placebo comparisons like-for-like: the placebo exposure is fitted by
exactly the code that fits the dose.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
import statsmodels.api as sm

import config as C


@dataclass
class Fit:
    """A fitted model, with the pieces the scripts actually use."""

    result: object
    names: list[str]
    frame: pd.DataFrame

    def term(self, name: str) -> dict:
        j = self.names.index(name)
        b = float(self.result.params[j])
        se = float(self.result.bse[j])
        return dict(term=name, coef=b, se=se,
                    lo=b - 1.96 * se, hi=b + 1.96 * se,
                    p=float(self.result.pvalues[j]),
                    odds_ratio=float(np.exp(b)),
                    n=len(self.frame), events=int(self.frame[C.OUTCOME].sum()))

    def difference(self, a: str, b: str) -> dict:
        """Difference between two coefficients of the same fit, with its
        standard error taken from the clustered covariance:
        Var(b_a - b_b) = V_aa + V_bb - 2 V_ab."""
        V = np.asarray(self.result.cov_params())
        i, j = self.names.index(a), self.names.index(b)
        d = float(self.result.params[i] - self.result.params[j])
        se = float(np.sqrt(V[i, i] + V[j, j] - 2 * V[i, j]))
        return dict(term=f"{a} - {b}", coef=d, se=se,
                    lo=d - 1.96 * se, hi=d + 1.96 * se,
                    n=len(self.frame), events=int(self.frame[C.OUTCOME].sum()))


def load(exploration_only: bool = True, asset_conditioned: bool = True
         ) -> pd.DataFrame:
    """Read the analysis frame and apply the sample definitions.

    exploration_only   drop the 28 cells held out before the models ran
    asset_conditioned  the M1 sample: events within 50 m of a road
    """
    d = pd.read_csv(C.DATA)
    if exploration_only:
        d = d[~d[C.CLUSTER].isin(C.HELD_OUT)]
    if asset_conditioned:
        d = d[(d[C.OUTCOME] == 0)
              | (d["road_band"].astype(str) == C.ROAD_BAND_M1)]
    return d.reset_index(drop=True)


def _dummies(d: pd.DataFrame, y: np.ndarray, column: str
             ) -> pd.DataFrame | None:
    """Indicator columns for a categorical covariate, pooling the levels
    too rare to identify (see config.MIN_LEVEL)."""
    s = d[column].astype(str).fillna("OTHER")
    keep = {lv for lv in s.unique()
            if ((s == lv) & (y == 1)).sum() >= C.MIN_LEVEL
            and ((s == lv) & (y == 0)).sum() >= C.MIN_LEVEL}
    s = s.where(s.isin(keep), "OTHER")
    if s.nunique() < 2:
        return None
    return pd.get_dummies(s, prefix=column, drop_first=True)


def fit(d: pd.DataFrame, exposure: str, extra: tuple[str, ...] = (),
        categorical: list[str] | None = None) -> Fit:
    """Fit equation (3) with `exposure` in the place of the transit dose.

    extra        further terms to carry alongside it
    categorical  which categorical covariates to include; the default is
                 both of them. The secondary specification M2 passes
                 ["lithology"], since it omits road class.
    """
    if categorical is None:
        categorical = list(C.CATEGORICAL)
    terms = [exposure] + list(extra) + C.COVARIATES
    terms = [t for t in terms if t in d.columns]
    d = d.dropna(subset=terms).reset_index(drop=True)
    y = d[C.OUTCOME].to_numpy(float)

    X, names = [np.ones(len(d))], ["const"]
    for t in terms:
        v = pd.to_numeric(d[t], errors="coerce").to_numpy(float)
        # a handful of observations have no climate value; they take the
        # median of the column rather than being dropped
        v = np.where(np.isfinite(v), v, np.nanmedian(v))
        X.append(v)
        names.append(t)
    for c in categorical:
        if True:
            if c not in d.columns:
                continue
            k = _dummies(d, y, c)
            if k is None:
                continue
            for col in k.columns:
                X.append(k[col].to_numpy(float))
                names.append(col)

    M = np.column_stack(X)
    # drop constant and linearly dependent columns, so that the fit is
    # identified whatever the slice
    const = [j for j in range(1, M.shape[1]) if np.ptp(M[:, j]) == 0]
    if const:
        keep = [j for j in range(M.shape[1]) if j not in const]
        M, names = M[:, keep], [names[j] for j in keep]
    _, R = np.linalg.qr(M)
    tol = 1e-9 * max(1.0, abs(R).max())
    keep = [j for j in range(M.shape[1]) if abs(R[j, j]) > tol]
    M, names = M[:, keep], [names[j] for j in keep]

    res = sm.Logit(y, M).fit(disp=0, method="bfgs", maxiter=500,
                             cov_type="cluster",
                             cov_kwds={"groups": d[C.CLUSTER].to_numpy()})
    return Fit(res, names, d)


def gate(d: pd.DataFrame) -> float:
    """Refit the primary specification and stop unless it is reproduced.

    Scripts call this before doing anything else. A result in this
    repository therefore comes from a run in which equation (3) still
    gave the coefficient the paper reports.
    """
    b = fit(d, C.DOSE).term(C.DOSE)["coef"]
    if abs(b - C.PRIMARY) > C.TOLERANCE:
        raise SystemExit(f"primary coefficient not reproduced: {b:+.4f} "
                         f"against {C.PRIMARY:+.4f}")
    print(f"gate: primary coefficient {b:+.4f}  ok")
    return b


def table(rows: list[dict], title: str, path) -> None:
    """Write rows as a Markdown table, the format the paper's own audit
    trail uses."""
    out = [f"# {title}", "",
           "| Model | Term | Coefficient | SE | 95% CI | p | n (events) |",
           "|---|---|---|---|---|---|---|"]
    for r in rows:
        p = "" if r.get("p") is None else f"{r['p']:.4f}"
        out.append(f"| {r.get('model', '')} | `{r['term']}` | "
                   f"{r['coef']:+.4f} | {r['se']:.4f} | "
                   f"{r['lo']:+.3f}, {r['hi']:+.3f} | {p} | "
                   f"{r['n']:,} ({r['events']}) |")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"written: {path.name}")
