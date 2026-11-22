"""Specification of the occurrence analysis, in one place.

Everything the models of the paper share lives here: the sample filters,
the covariate set, the clustering, and the list of cells held out before
the models were run. Changing a model means changing this file, not
hunting through the scripts.
"""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent

DATA = Path(os.environ.get("ROCKFALL_FRAME",
                           ROOT.parent / "data" / "analysis_frame.csv"))
"""The analysis frame. It is not published with this code, because the
permission covering the two institutional databases behind it extends to
their use in research and not to their redistribution. `ANALYSIS_FRAME.md`
describes the table column by column; point ROCKFALL_FRAME at your own
copy to run the scripts."""

OUT = Path(os.environ.get("ROCKFALL_RESULTS", ROOT.parent / "results"))

# ---------------------------------------------------------------- outcome
OUTCOME = "event"
CLUSTER = "cluster"

# ------------------------------------------------------------- exposures
DOSE = "dose_transit"
"""The primary exposure: forested share of the transit window, D_tr."""

PLACEBO = "forest_below_500m"
"""The placebo exposure F↓: forest below the point, which cannot stop a
block that has already reached the road."""

COMPARATOR = "forest_above_500m"
"""F↑: the same measure above the point. Mechanistically admissible, so a
comparator rather than a placebo."""

# ------------------------------------------------------------- covariates
GEOMETRY = ["log_drop", "log_run", "slope_max", "slope_sd"]
ENVIRONMENT = ["elevation_m", "pga_475", "freeze_thaw_days"]
SOURCE = ["source_bare_rock"]
CATEGORICAL = ["lithology", "road_class"]

COVARIATES = ["dose_source"] + GEOMETRY + ENVIRONMENT + SOURCE
"""The source-side dose and the terrain, seismic and climate covariates of
equation (3). The exposure under test is added to the front of this list
by `model.fit`."""

TERRAIN_BELOW = ["relief_below_m", "gradient_below_deg", "slope_position"]
"""Section 3.6: measures of the ground below the point, used to ask
whether the placebo exposure is a terrain proxy."""

REPORTING_PROXIES = ["dist_settlement_m", "dist_residential_m",
                     "dist_trunk_m"]
"""Section 3.6: distances entered in logs as proxies for the reporting
process."""

# ----------------------------------------------------------------- sample
ROAD_BAND_M1 = "<50"
"""The asset-conditioned sample keeps events within 50 m of a road.
Controls lie on a road line by construction and are all retained."""

MIN_LEVEL = 10
"""A categorical level is kept only where it carries at least this many
events and this many controls. A level present in one group alone
separates the outcome perfectly. In this sample exactly one lithological
class meets the rule, so lithology enters as a single indicator."""

HELD_OUT = """
47_84 48_88 50_85 50_90 51_86 51_87 52_89 53_92 54_84 55_92
60_82 60_90 63_90 64_82 64_89 65_89 66_83 66_86 66_89 67_83
68_83 68_86 68_87 69_84 69_85 69_86 69_90 70_89
""".split()
"""The 28 cluster cells set aside with a fixed seed before any model was
fitted. Results in the paper are reported on the remaining cells, called
the exploration slice; Section 3.3 reports the held-out slice once."""

# ------------------------------------------------------------- benchmarks
PRIMARY = -1.1967
"""The coefficient of the primary specification. Scripts that build on it
check it first and stop if it is not reproduced, so a result can never be
reported from a run in which the primary estimate had moved."""

TOLERANCE = 0.003
