# Glossary

The full analysis was run in Turkish and the files in `audit_tables/` carry Turkish headings. The published code in `code/` is in English; this is the correspondence.

*Generated 2026-11-22.*

### Variables in the audit tables

| Turkish | English |
|---|---|
| `doz_gecis` | transit dose D_tr; `dose_transit` in `data/` |
| `doz_ust` | source-side dose D_up; `dose_source` |
| `kom_asagi_500m` | forest below the point; `forest_below_500m` |
| `kom_yukari_500m` | forest above the point; `forest_above_500m` |
| `logdh / logL` | log drop height / log horizontal distance |
| `beta` | inferred maximum energy line angle, arctan(dh/L) |
| `olay / vaka / kontrol` | event / case / control |
| `kume` | 50 km cluster cell |
| `kaynak_kayalik` | bare rock at the inferred release cell |
| `guzergah_egim_maks / _sd` | along-path maximum slope / dispersion |
| `yol_sinifi / yol_bandi` | road class / road distance band |
| `mescere` | forest stand |
| `tahsis` | designation of a protective function |

### Table headings

| Turkish | English |
|---|---|
| `katsayi, katsayı` | coefficient |
| `SE` | standard error |
| `%95 GA` | 95% confidence interval |
| `OR` | odds ratio |
| `n (olay)` | n (events) |
| `terim / model` | term / model |
| `olcum, ölçüm / deger, değer` | measurement / value |
| `medyan / ortalama` | median / mean |
| `esik / bolge / sonuc / pay` | threshold / region / result / share |

### Words in the run logs

| Turkish | English |
|---|---|
| `KARAR` | decision: which branch of the pre-registered rule the result fell into |
| `OKUMA KURALI` | reading rule, written before the run |
| `kapi` | gate: a check that stops the script unless the primary coefficient is reproduced |
| `kesif dilimi / ayrilan dilim` | exploration slice / held-out slice |
| `ozgulluk / plasebo / dayaniklilik` | specificity / placebo / robustness |
| `bildirim` | reporting |
