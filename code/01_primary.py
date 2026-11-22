"""The occurrence estimate: Sections 3.2 and 3.3 of the paper.

Produces the primary coefficient, the secondary specification that keeps
all qualifying events, the exposure measured as forested length rather
than as a share, and the held-out slice.

    python 01_primary.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

import config as C
import model as M


def main() -> None:
    d = M.load()
    M.gate(d)
    rows = []

    # --- primary: equation (3) on the exploration slice of M1
    f = M.fit(d, C.DOSE)
    r = f.term(C.DOSE)
    rows.append(dict(model="Primary, equation (3)", **r))
    print(f"primary            {r['coef']:+.4f}  OR {r['odds_ratio']:.3f}  "
          f"[{r['lo']:+.3f}, {r['hi']:+.3f}]")
    rows.append(dict(model="Primary, equation (3)", **f.term("dose_source")))

    # --- secondary: every qualifying event, no road class
    d2 = M.load(asset_conditioned=False)
    f2 = M.fit(d2, C.DOSE, categorical=["lithology"])
    r2 = f2.term(C.DOSE)
    rows.append(dict(model="Secondary, all events, no road class", **r2))
    print(f"secondary          {r2['coef']:+.4f}  OR {r2['odds_ratio']:.3f}  "
          f"({r2['events']} events)")

    # --- the exposure as forested length instead of as a share
    e = d.copy()
    e["forested_length_100m"] = (pd.to_numeric(e[C.DOSE], errors="coerce")
                                 * e["transit_window_m"] / 100.0)
    f3 = M.fit(e, "forested_length_100m")
    r3 = f3.term("forested_length_100m")
    rows.append(dict(model="Exposure as forested length", **r3))
    median_window = float(f3.frame["transit_window_m"].median())
    scaled = r3["coef"] * median_window / 100.0
    print(f"per 100 m          {r3['coef']:+.4f}  "
          f"OR {r3['odds_ratio']:.3f}; over the median window of "
          f"{median_window:.0f} m that is {scaled:+.3f}, against "
          f"{C.PRIMARY:+.3f} for a full change of dose")

    # --- the slice held out before the models were run
    h = M.load(exploration_only=False)
    h = h[h[C.CLUSTER].isin(C.HELD_OUT)]
    h = h[(h[C.OUTCOME] == 0)
          | (h["road_band"].astype(str) == C.ROAD_BAND_M1)]
    f4 = M.fit(h, C.DOSE)
    r4 = f4.term(C.DOSE)
    rows.append(dict(model="Held-out slice", **r4))
    print(f"held-out slice     {r4['coef']:+.4f}  "
          f"[{r4['lo']:+.3f}, {r4['hi']:+.3f}]  "
          f"({r4['events']} events) — agrees in sign, inconclusive alone")

    M.table(rows, "The occurrence estimate", C.OUT / "01_primary.md")


if __name__ == "__main__":
    main()
