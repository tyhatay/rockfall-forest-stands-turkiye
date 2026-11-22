# Specificity of the occurrence estimate

| Model | Term | Coefficient | SE | 95% CI | p | n (events) |
|---|---|---|---|---|---|---|
| Placebo in place of the dose | `forest_below_500m` | -2.1116 | 0.2863 | -2.673, -1.550 | 0.0000 | 3,394 (159) |
| Both together | `dose_transit` | -0.6689 | 0.4100 | -1.473, +0.135 | 0.1028 | 3,394 (159) |
| Both together | `forest_below_500m` | -1.8852 | 0.3481 | -2.567, -1.203 | 0.0000 | 3,394 (159) |
| Each alone, per SD | `z_dose_transit` | -0.5272 | 0.1574 | -0.836, -0.219 | 0.0008 | 3,394 (159) |
| Each alone, per SD | `z_forest_below_500m` | -0.7849 | 0.1064 | -0.993, -0.576 | 0.0000 | 3,394 (159) |
| Each alone, per SD | `z_forest_above_500m` | -0.3599 | 0.1614 | -0.676, -0.044 | 0.0258 | 3,394 (159) |
| Both together, per SD | `z_dose_transit` | -0.2949 | 0.1807 | -0.649, +0.059 | 0.1027 | 3,394 (159) |
| Both together, per SD | `z_forest_below_500m` | -0.7008 | 0.1294 | -0.954, -0.447 | 0.0000 | 3,394 (159) |
| Difference, per SD | `z_forest_below_500m - z_dose_transit` | -0.4059 | 0.2788 | -0.952, +0.140 |  | 3,394 (159) |
| All three together, per SD | `z_dose_transit` | -0.4254 | 0.1859 | -0.790, -0.061 | 0.0221 | 3,394 (159) |
| All three together, per SD | `z_forest_below_500m` | -0.8283 | 0.1674 | -1.156, -0.500 | 0.0000 | 3,394 (159) |
| All three together, per SD | `z_forest_above_500m` | +0.3590 | 0.2387 | -0.109, +0.827 | 0.1326 | 3,394 (159) |
| Below and above, per SD | `z_forest_below_500m` | -0.8486 | 0.1636 | -1.169, -0.528 | 0.0000 | 3,394 (159) |
| Below and above, per SD | `z_forest_above_500m` | +0.1424 | 0.2282 | -0.305, +0.590 | 0.5327 | 3,394 (159) |
| Difference, below − above | `z_forest_below_500m - z_forest_above_500m` | -0.9910 | 0.3697 | -1.716, -0.266 |  | 3,394 (159) |
| Dose, with terrain below | `dose_transit` | -1.1677 | 0.3541 | -1.862, -0.474 | 0.0010 | 3,394 (159) |
| Placebo, with terrain below | `forest_below_500m` | -2.3038 | 0.2670 | -2.827, -1.780 | 0.0000 | 3,394 (159) |
| Terrain term itself | `relief_below_m` | -0.0016 | 0.0036 | -0.009, +0.006 | 0.6660 | 3,394 (159) |
| Terrain term itself | `gradient_below_deg` | +0.1139 | 0.0631 | -0.010, +0.238 | 0.0710 | 3,394 (159) |
| Terrain term itself | `slope_position` | -1.3177 | 1.8763 | -4.995, +2.360 | 0.4825 | 3,394 (159) |
| Dose, with reporting proxies | `dose_transit` | -1.3356 | 0.3677 | -2.056, -0.615 | 0.0003 | 3,395 (159) |
| Both, with reporting proxies | `dose_transit` | -0.7354 | 0.4073 | -1.534, +0.063 | 0.0710 | 3,394 (159) |
| Both, with reporting proxies | `forest_below_500m` | -2.0606 | 0.3397 | -2.726, -1.395 | 0.0000 | 3,394 (159) |
| Within strata | `dose_transit` | -0.6654 | 0.3807 | -1.411, +0.081 | 0.0805 | 3,394 (159) |
| Within strata, placebo carried | `dose_transit` | -0.6500 | 0.3848 | -1.404, +0.104 | 0.0912 | 3,394 (159) |
| Dose by road class | `dose_transit` | -1.0861 | 0.3440 | -1.760, -0.412 | 0.0016 | 3,395 (159) |
| Dose by road class | `dose_x_track` | -1.4209 | 0.6524 | -2.700, -0.142 | 0.0294 | 3,395 (159) |
| Dose, region excluded | `dose_transit` | -0.8520 | 0.4091 | -1.654, -0.050 | 0.0373 | 2,209 (75) |
| Placebo, region excluded | `forest_below_500m` | -2.7651 | 0.4909 | -3.727, -1.803 | 0.0000 | 2,208 (75) |
| dose × region | `x_region` | +0.2196 | 0.4613 | -0.685, +1.124 | 0.6340 | 3,395 (159) |
| placebo × region | `x_region` | +1.7051 | 0.4932 | +0.738, +2.672 | 0.0005 | 3,394 (159) |

## Notes

- Dose and placebo exposure are correlated at 0.576, so the joint fit divides a signal they share.

- Standard deviations on the observations where all three are measured: dose_transit 0.4408, forest_below_500m 0.3717, forest_above_500m 0.3450.

- The transit dose is left out of that fit because it is correlated with the uphill share at 0.823; the two neighbourhoods are correlated at 0.693.

- Five quantile bins were asked for; ties collapse them into 4 unequal strata. Stratum [3] contains no event, so it contributes nothing to the likelihood and the fit rests on 2,715 observations. Within-stratum SD of the dose is 0.363 against 0.441 over the slice.

- Tracks carry 11 of the events, so the interaction is wide.
