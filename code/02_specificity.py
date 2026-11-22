"""Is the occurrence estimate specific to the transit zone? Section 3.6.

Runs every test the paper reports in Table 6, in the order the argument
develops:

  1  the placebo exposure fitted in place of the dose, and alongside it
  2  both on a common scale, since one is a share of a line and the
     other a share of an area
  3  the same neighbourhood measured on the uphill side, which is a
     comparator rather than a placebo
  4  the terrain below the point, in case neither forest nor reporting
     is the operative quantity
  5  proxies for the reporting process
  6  the estimate within strata of surrounding woodedness
  7  the dose allowed to differ by road class
  8  the eastern Black Sea window excluded

    python 02_specificity.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

import config as C
import model as M


def main() -> None:
    d = M.load()
    M.gate(d)
    rows, notes = [], []

    def add(model, fit, *terms):
        for t in terms:
            r = fit.term(t)
            rows.append(dict(model=model, **r))
            print(f"  {model:34s} {t:22s} {r['coef']:+8.4f} "
                  f"[{r['lo']:+7.3f}, {r['hi']:+7.3f}]")

    # ---------------------------------------------- 1 · the placebo exposure
    print("\n1. the placebo exposure")
    add("Placebo in place of the dose", M.fit(d, C.PLACEBO), C.PLACEBO)
    joint = M.fit(d, C.DOSE, extra=(C.PLACEBO,))
    add("Both together", joint, C.DOSE, C.PLACEBO)
    r = d[[C.DOSE, C.PLACEBO]].corr().iloc[0, 1]
    notes.append(f"Dose and placebo exposure are correlated at {r:.3f}, so "
                 f"the joint fit divides a signal they share.")

    # ------------------------------------------------------ 2 · common scale
    print("\n2. on a common scale")
    both = [C.DOSE, C.PLACEBO, C.COMPARATOR]
    s = d.dropna(subset=both + C.COVARIATES).copy()
    sd = {c: float(s[c].std()) for c in both}
    for c in both:
        s["z_" + c] = s[c] / sd[c]
    notes.append("Standard deviations on the observations where all three "
                 "are measured: " + ", ".join(f"{c} {sd[c]:.4f}"
                                              for c in both) + ".")
    for c in both:
        add("Each alone, per SD", M.fit(s, "z_" + c), "z_" + c)
    z2 = M.fit(s, "z_" + C.DOSE, extra=("z_" + C.PLACEBO,))
    add("Both together, per SD", z2, "z_" + C.DOSE, "z_" + C.PLACEBO)
    dif = z2.difference("z_" + C.PLACEBO, "z_" + C.DOSE)
    rows.append(dict(model="Difference, per SD", **dif))
    print(f"  {'difference placebo - dose':<34} {'':22s} "
          f"{dif['coef']:+8.4f} [{dif['lo']:+7.3f}, {dif['hi']:+7.3f}]"
          + ("  covers zero" if dif["lo"] < 0 < dif["hi"] else ""))
    z3 = M.fit(s, "z_" + C.DOSE,
               extra=("z_" + C.PLACEBO, "z_" + C.COMPARATOR))
    add("All three together, per SD", z3,
        "z_" + C.DOSE, "z_" + C.PLACEBO, "z_" + C.COMPARATOR)

    # ------------------------------------------- 3 · the two sides compared
    print("\n3. the two sides of the point, same instrument")
    sides = M.fit(s, "z_" + C.PLACEBO, extra=("z_" + C.COMPARATOR,))
    add("Below and above, per SD", sides,
        "z_" + C.PLACEBO, "z_" + C.COMPARATOR)
    dif2 = sides.difference("z_" + C.PLACEBO, "z_" + C.COMPARATOR)
    rows.append(dict(model="Difference, below − above", **dif2))
    print(f"  {'difference below - above':<34} {'':22s} "
          f"{dif2['coef']:+8.4f} [{dif2['lo']:+7.3f}, {dif2['hi']:+7.3f}]")
    notes.append("The transit dose is left out of that fit because it is "
                 f"correlated with the uphill share at "
                 f"{d[[C.DOSE, C.COMPARATOR]].corr().iloc[0, 1]:.3f}; the "
                 "two neighbourhoods are correlated at "
                 f"{d[[C.PLACEBO, C.COMPARATOR]].corr().iloc[0, 1]:.3f}.")

    # --------------------------------------------- 4 · terrain below the point
    print("\n4. terrain below the point")
    add("Dose, with terrain below", M.fit(d, C.DOSE, extra=tuple(
        C.TERRAIN_BELOW)), C.DOSE)
    t_pl = M.fit(d, C.PLACEBO, extra=tuple(C.TERRAIN_BELOW))
    add("Placebo, with terrain below", t_pl, C.PLACEBO)
    for t in C.TERRAIN_BELOW:
        rows.append(dict(model="Terrain term itself", **t_pl.term(t)))

    # ---------------------------------------------- 5 · reporting proxies
    print("\n5. proxies for the reporting process")
    p = d.copy()
    logs = []
    for c in C.REPORTING_PROXIES:
        p["log_" + c] = np.log1p(pd.to_numeric(p[c], errors="coerce")
                                 .clip(lower=0))
        logs.append("log_" + c)
    add("Dose, with reporting proxies", M.fit(p, C.DOSE, extra=tuple(logs)),
        C.DOSE)
    add("Both, with reporting proxies",
        M.fit(p, C.DOSE, extra=(C.PLACEBO,) + tuple(logs)),
        C.DOSE, C.PLACEBO)

    # ------------------------------------------------------- 6 · strata
    print("\n6. within strata of surrounding woodedness")
    st = d.dropna(subset=[C.PLACEBO, C.DOSE]).copy()
    st["stratum"] = pd.qcut(st[C.PLACEBO], 5, labels=False,
                            duplicates="drop")
    counts = st.groupby("stratum")[C.OUTCOME].agg(["size", "sum"])
    print("  strata (n, events):",
          {int(i): (int(a), int(b)) for i, (a, b) in counts.iterrows()})
    empty = counts.index[counts["sum"] == 0].tolist()
    dummies = pd.get_dummies(st["stratum"], prefix="stratum",
                             drop_first=True).astype(float)
    for c in dummies.columns:
        st[c] = dummies[c].to_numpy()
    add("Within strata", M.fit(st, C.DOSE, extra=tuple(dummies.columns)),
        C.DOSE)
    add("Within strata, placebo carried",
        M.fit(st, C.DOSE, extra=(C.PLACEBO,) + tuple(dummies.columns)),
        C.DOSE)
    within = st.groupby("stratum")[C.DOSE].transform("mean")
    kept = st[~st["stratum"].isin(empty)]
    notes.append(
        f"Five quantile bins were asked for; ties collapse them into "
        f"{st['stratum'].nunique()} unequal strata. "
        f"{'Stratum ' + str(empty) + ' contains no event, so it contributes nothing to the likelihood and the fit rests on ' + format(len(kept), ',') + ' observations. ' if empty else ''}"
        f"Within-stratum SD of the dose is "
        f"{(st[C.DOSE] - within).std():.3f} against {st[C.DOSE].std():.3f} "
        f"over the slice.")

    # --------------------------------------------------- 7 · road class
    print("\n7. the dose by road class")
    rc = d.copy()
    rc["track"] = rc["road_class"].astype(str).str.startswith("track")\
        .astype(float)
    rc["dose_x_track"] = rc[C.DOSE] * rc["track"]
    add("Dose by road class", M.fit(rc, C.DOSE,
                                    extra=("track", "dose_x_track")),
        C.DOSE, "dose_x_track")
    notes.append("Tracks carry "
                 f"{int(rc.loc[rc.track == 1, C.OUTCOME].sum())} of the "
                 "events, so the interaction is wide.")

    # ------------------------------------------------------- 8 · region
    print("\n8. the eastern Black Sea window excluded")
    out = d[d["black_sea_window"] == 0]
    add("Dose, region excluded", M.fit(out, C.DOSE), C.DOSE)
    add("Placebo, region excluded", M.fit(out, C.PLACEBO), C.PLACEBO)
    rc2 = d.copy()
    for name, exp in (("dose", C.DOSE), ("placebo", C.PLACEBO)):
        rc2["x_region"] = rc2[exp] * rc2["black_sea_window"]
        f = M.fit(rc2, exp, extra=("black_sea_window", "x_region"))
        r = f.term("x_region")
        rows.append(dict(model=f"{name} × region", **r))
        print(f"  {name + ' x region':<34} {'':22s} {r['coef']:+8.4f} "
              f"p={r['p']:.4g}")

    M.table(rows, "Specificity of the occurrence estimate",
            C.OUT / "02_specificity.md")
    with open(C.OUT / "02_specificity.md", "a", encoding="utf-8") as fh:
        fh.write("\n## Notes\n\n" + "\n\n".join(f"- {n}" for n in notes)
                 + "\n")


if __name__ == "__main__":
    main()
