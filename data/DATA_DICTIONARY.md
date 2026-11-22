# The analysis frame — column dictionary

The table `code/` reads. It is derived from the two institutional databases behind the study but reproduces neither: it holds the variables the published models are fitted on and nothing else, so that the estimates can be checked and the specification compared against the paper.

It has 4,175 rows, one per observation: 343 recorded events and 3832 road-network control points.

| Column | Meaning |
|---|---|
| `event` | 1 for a recorded rockfall, 0 for a road-network control point |
| `cluster` | 50 km grid cell; standard errors are clustered on this |
| `road_band` | distance band from the point to the nearest road; the asset-conditioned sample M1 keeps events in the <50 m band |
| `road_class` | OpenStreetMap class of the nearest road |
| `lithology` | lithological unit code, 1:500,000 national geological map |
| `dose_transit` | D_tr of equation (2): forested share of the transit window, the primary exposure |
| `dose_source` | D_up of equation (2): forested share of the source-side window |
| `forest_below_500m` | F↓ of equation (6): forested share of the 500 m neighbourhood below the point; the placebo exposure |
| `forest_above_500m` | F↑: the same measure above the point; a comparator, not a placebo |
| `forest_500m` | forested share of the whole 500 m neighbourhood, undirected |
| `forest_250m` | forested share of the 250 m neighbourhood |
| `transit_window_m` | length of the transit window, m; with dose_transit it gives the forested length, which Section 3.4 reports per 100 m |
| `log_drop` | log drop height, log Δh |
| `log_run` | log horizontal distance, log L |
| `slope_max` | maximum slope along the line, degrees |
| `slope_sd` | standard deviation of slope along the line, degrees |
| `elevation_m` | elevation at the point, m |
| `pga_475` | peak ground acceleration, 475-year return period |
| `freeze_thaw_days` | annual freeze–thaw days |
| `source_bare_rock` | bare-rock flag at the inferred release cell |
| `relief_below_m` | relief below the point within 500 m, m |
| `gradient_below_deg` | mean downhill gradient to the grid samples below the point, degrees |
| `slope_position` | position of the point within the local range of elevation, 0 = bottom |
| `dist_settlement_m` | distance to the nearest settlement polygon, m |
| `dist_residential_m` | distance to the nearest residential-class road, m |
| `dist_trunk_m` | distance to the nearest trunk road, m |
| `black_sea_window` | 1 if the point falls in the eastern Black Sea window used in Section 3.4 (37.5–42.5° E, 40.0–42.2° N); the coordinates themselves are not released |

## What the table does not contain

Even in its unpublished form it carries no coordinate, no record identifier, no date, no province, district or locality name, no free-text field or any flag derived from one, no stand symbol and no polygon attribute: only the variables the models are fitted on. The cluster label names a 50 km grid cell, which is what the standard errors are clustered on.

## Obtaining the data

The rockfall incident inventory is held by the Disaster and Emergency Management Presidency (AFAD) and the stand database by the General Directorate of Forestry (OGM). Both are available to researchers on application to those institutions. The open datasets the analysis also uses are listed in Table 1 of the paper, each with its distributor.
