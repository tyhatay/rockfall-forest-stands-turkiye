# Forest and recorded rockfall in Türkiye

Reproduction package for the study *Forest and recorded rockfall in
Türkiye: two estimates, two placebos, and what an incident inventory can
identify*.

The study builds two estimates of forest's effect on rockfall from one
national incident inventory, shows that both survive the robustness
checks such results are normally given, and then shows that neither
survives a test of specificity: an exposure that cannot act on a block
predicts a recorded event as well as the exposure that can. A simulation
establishes that the test is able to pass when protection is the only
thing operating, so what fails is identification rather than power.

## What is here

| Folder | Contents |
|---|---|
| `code/` | five files that produce the estimates |
| `data/` | `analysis_frame.csv`, the variables the published models are fitted on, with `DATA_DICTIONARY.md` |
| `results/` | what that code wrote when we ran it, 4 files |
| `figures/` | the five figures of the paper |
| `audit_tables/` | the 51 measurement files of the full analysis, in Turkish, so that every number in the paper can be traced to the run that produced it; `INDEX.md` lists them in English and `GLOSSARY.md` gives the terms |

`code/` is a deliberate selection rather than the working tree. The full
analysis ran to some two hundred scripts over several iterations, most of
them superseded; what is published here is the part that produces the
published estimates, written in English so that it can be read.

`config.py` holds the specification in one place: the exposure, the
covariates, the clustering, the rule for pooling rare categorical levels,
the cells held out before the models were run, and the primary
coefficient. `model.py` holds `fit`, the routine every estimate in the
paper goes through — the placebo exposure is fitted by exactly the code
that fits the dose, which is what makes the comparison like for like —
and `gate`, which refits the primary specification and stops unless it
reproduces −1.1967 to within 0.003. Then:

| Script | Produces |
|---|---|
| `01_primary.py` | the primary coefficient, the secondary specification, the exposure as forested length, and the held-out slice (Sections 3.2 and 3.3) |
| `02_specificity.py` | the eight tests of Section 3.6, in the order the argument develops; this is Table 6 of the paper |
| `03_power.py` | the three simulated worlds behind Figure 5c |

## Run it

```bash
cd code
python 01_primary.py        # Sections 3.2 and 3.3
python 02_specificity.py    # Section 3.6, Table 6
python 03_power.py          # Section 3.6, Figure 5c  (a few minutes)
```

Python 3.11 or later with `pandas`, `numpy` and `statsmodels`. Nothing
else is needed: the scripts read `data/analysis_frame.csv` and write
their tables into `results/`. Set `ROCKFALL_FRAME` to read the frame from
somewhere else.

## What the code produced here

| Quantity | In the paper | In `results/` |
|---|---|---|
| Transit dose, equation (3) | −1.197 (−1.896, −0.497) | `01_primary.md` |
| Placebo exposure in its place | −2.112 (−2.673, −1.550) | `02_specificity.md` |
| Both together, transit dose | −0.669 (−1.473, +0.135) | `02_specificity.md` |
| Per standard deviation, placebo − dose | −0.406 (−0.952, +0.140) | `02_specificity.md` |
| Below minus above the point, per SD | −0.991 (−1.716, −0.266) | `02_specificity.md` |
| Draws from a protective world reaching the observed placebo | none of 200 | `03_power.md` |

## The data

The study uses two institutional databases at full national coverage: the
national rockfall incident inventory held by the Disaster and Emergency
Management Presidency (AFAD) and the national forest management database
held by the General Directorate of Forestry (OGM). Both are used under
institutional permission for scientific research, and **neither is
redistributed here**: no record, no polygon, no stand symbol.

What is published is the derived table the models are fitted on. It holds
one row per observation and only the variables those models use, with
**no coordinate, no record identifier, no date, no province, district or
locality name, no free-text field and no stand symbol**. For the regional
check of Section 3.4 it carries a single flag rather than a position, and
the cluster label names a 50 km grid cell, which localises an observation
no more finely than the map published as Figure 1. Readers who need the
primary data should apply to the holding institutions, which make it
available to researchers.

The open datasets the analysis also uses — FABDEM, Global Forest Change,
the global canopy height model, CORINE, ERA5-Land, CHELSA, the GEM hazard
map and OpenStreetMap — are not mirrored here; each is obtained from its
own distributor under its own licence, and the mandatory attributions are
given in the paper.

## Licence

The code is released under the MIT Licence. The figures, the results
and the audit tables are derived statistics computed from data used under
institutional permission; they are published so that the results of the
paper can be checked, and no claim of ownership over the underlying
databases is made or implied.

Repository: <https://github.com/tyhatay/rockfall-forest-stands-turkiye>

*Generated 2026-11-22.*
