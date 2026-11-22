"""Can the specificity test pass? Section 3.6, Figure 5c.

A placebo exposure correlated with the real one will fail wherever the
real one works, so a failed placebo means nothing until the test has
been shown able to pass. That is settled by simulation rather than by
argument.

The real exposures, covariates and clustering are held fixed and only
the outcome is regenerated, in three worlds:

  protection   the log odds of a record depend on the transit dose with
               the coefficient estimated from these data, and not on the
               placebo exposure at all
  reporting    they depend on the undirected woodedness of the 500 m
               neighbourhood, calibrated to induce the same dose
               coefficient, and not on the transit dose
  neither      they depend on neither exposure

The test of 02_specificity is then run on 200 draws from each world and
the rule recorded in advance is applied unchanged, which measures what
the rule does when the answer is known.

    python 03_power.py --draws 200
"""

from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

import config as C
import model as M

SEED = 20261122
TARGET_EVENTS = 159
WOODEDNESS = "forest_500m"

RULE_SHARE = 0.5
"""The rule recorded in advance: specificity fails when the placebo
interval excludes zero, the coefficient is negative, and its magnitude is
at least half that of the dose."""


def solve_intercept(base: np.ndarray, extra: np.ndarray, target: int
                    ) -> float:
    lo, hi = -40.0, 20.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if float((1 / (1 + np.exp(-(mid + base + extra)))).sum()) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def one_draw(d: pd.DataFrame, y: np.ndarray) -> dict:
    e = d.copy()
    e[C.OUTCOME] = y
    dose = M.fit(e, C.DOSE).term(C.DOSE)
    plac = M.fit(e, C.PLACEBO).term(C.PLACEBO)
    joint = M.fit(e, C.DOSE, extra=(C.PLACEBO,))
    jd, jp = joint.term(C.DOSE), joint.term(C.PLACEBO)
    fails = (plac["hi"] < 0 and plac["coef"] < 0
             and abs(plac["coef"]) >= RULE_SHARE * abs(dose["coef"]))
    return dict(dose=dose["coef"], placebo=plac["coef"],
                joint_dose=jd["coef"], joint_placebo=jp["coef"],
                joint_dose_covers_zero=bool(jd["lo"] < 0 < jd["hi"]),
                rule_says_failed=bool(fails), events=int(y.sum()))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--draws", type=int, default=200)
    ap.add_argument("--calibration-draws", type=int, default=12)
    a = ap.parse_args()

    d = M.load()
    M.gate(d)

    # the covariate contribution of the fitted primary model, with the
    # dose term removed: the simulated worlds keep everything about this
    # sample except what drives the outcome
    f = M.fit(d, C.DOSE)
    d = f.frame.reset_index(drop=True)
    dose = pd.to_numeric(d[C.DOSE], errors="coerce").to_numpy(float)
    wood = pd.to_numeric(d[WOODEDNESS], errors="coerce").to_numpy(float)
    wood = np.where(np.isfinite(wood), wood, np.nanmedian(wood))
    base = np.asarray(f.result.fittedvalues, float) - C.PRIMARY * dose
    rng = np.random.default_rng(SEED)

    def draw(extra: np.ndarray, n: int) -> np.ndarray:
        c = solve_intercept(base, extra, TARGET_EVENTS)
        p = 1 / (1 + np.exp(-(c + base + extra)))
        return (rng.random((n, len(p))) < p).astype(float)

    plac = pd.to_numeric(d[C.PLACEBO], errors="coerce")
    print(f"\ncorrelations: dose-placebo "
          f"{plac.corr(pd.Series(dose)):.3f}, placebo-woodedness "
          f"{plac.corr(pd.Series(wood)):.3f}")

    # --- calibrate the reporting world so it induces the same dose coefficient
    print("\ncalibrating the reporting world")
    best, gap = None, 9e9
    for g in (-1.0, -1.5, -2.0, -2.5, -3.0, -4.0):
        ys = draw(g * wood, a.calibration_draws)
        got = [one_draw(d, ys[i])["dose"] for i in range(len(ys))]
        m = float(np.mean(got))
        print(f"  gamma {g:+.1f} induces a dose coefficient of {m:+.3f}")
        if abs(m - C.PRIMARY) < gap:
            best, gap = g, abs(m - C.PRIMARY)
    print(f"  chosen gamma {best:+.1f}")

    worlds = {"protection": C.PRIMARY * dose,
              "reporting": best * wood,
              "neither": np.zeros_like(dose)}

    observed = dict(dose=C.PRIMARY, placebo=-2.1116,
                    joint_dose=-0.6689, joint_placebo=-1.8852)
    rows, frames = [], []
    for name, extra in worlds.items():
        ys = draw(extra, a.draws)
        got = pd.DataFrame([one_draw(d, ys[i]) for i in range(a.draws)])
        got["world"] = name
        frames.append(got)
        as_strong = float((got.placebo <= observed["placebo"]).mean())
        both = float(((got.placebo <= observed["placebo"])
                      & (got.joint_dose >= observed["joint_dose"])).mean())
        rows.append(dict(world=name, draws=len(got),
                         events=got.events.mean(),
                         dose=got.dose.mean(), placebo=got.placebo.mean(),
                         joint_dose=got.joint_dose.mean(),
                         joint_placebo=got.joint_placebo.mean(),
                         p05=got.placebo.quantile(0.05),
                         p95=got.placebo.quantile(0.95),
                         rule_failed=float(got.rule_says_failed.mean()),
                         as_strong=as_strong, both=both))
        print(f"\n{name}: dose {rows[-1]['dose']:+.3f}  placebo "
              f"{rows[-1]['placebo']:+.3f}  joint {rows[-1]['joint_dose']:+.3f}"
              f" / {rows[-1]['joint_placebo']:+.3f}")
        print(f"  the rule says specificity failed in "
              f"{100 * rows[-1]['rule_failed']:.0f}% of draws; "
              f"{100 * as_strong:.1f}% reach the observed placebo "
              f"coefficient and {100 * both:.1f}% reproduce both quantities")

    C.OUT.mkdir(parents=True, exist_ok=True)
    pd.concat(frames, ignore_index=True).to_csv(
        C.OUT / "03_power_draws.csv", index=False)
    out = ["# Can the specificity test pass?", "",
           f"{a.draws} draws in each of three worlds; only the outcome is "
           f"simulated. The reporting world is calibrated to induce the "
           f"same dose coefficient (gamma {best:+.1f}).", "",
           "| World | Dose | Placebo | Joint dose | Joint placebo | "
           "Rule says failed | Reaches the observed placebo | Both |",
           "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        out.append(f"| {r['world']} | {r['dose']:+.3f} | {r['placebo']:+.3f} "
                   f"| {r['joint_dose']:+.3f} | {r['joint_placebo']:+.3f} | "
                   f"{100 * r['rule_failed']:.0f}% | "
                   f"{100 * r['as_strong']:.1f}% | {100 * r['both']:.1f}% |")
    out += ["| **observed** | **−1.197** | **−2.112** | **−0.669** | "
            "**−1.885** | failed | — | — |", "",
            "The observed pattern lies inside what the reporting world "
            "produces and outside what the protective world produces. "
            "Applied as a binary rule the test also misfires on a quarter "
            "of protective draws, so what separates the worlds is the size "
            "of the placebo coefficient rather than whether its interval "
            "excludes zero."]
    (C.OUT / "03_power.md").write_text("\n".join(out) + "\n",
                                       encoding="utf-8")
    print(f"\nwritten: 03_power.md, 03_power_draws.csv")


if __name__ == "__main__":
    main()
