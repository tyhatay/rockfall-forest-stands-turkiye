# 33 — siklik orneklemi: betimleme ve katsayilar

## Betimleme (tam cerceve, vaka / kontrol)

| ölçüm | medyan | ortalama | SMD |
|---|---|---|---|
| β (°) | 32.208 / 31.562 | 32.764 / 32.598 | +0.04 |
| L (m) | 282.840 / 294.673 | 362.568 / 366.017 | -0.02 |
| Δh (m) | 184.000 / 187.000 | 229.676 / 231.660 | -0.01 |
| transit dose | 0.435 / 0.882 | 0.458 / 0.611 | -0.34 |
| source-side dose | 0.800 / 1.000 | 0.592 / 0.698 | -0.24 |
| along-path max slope (°) | 42.867 / 41.636 | 44.443 / 43.587 | +0.12 |
| along-path slope SD (°) | 7.931 / 7.394 | 8.415 / 7.806 | +0.16 |
| elevation (m) | 923.000 / 866.000 | 930.163 / 915.748 | +0.03 |
| bare rock at source | 0.000 / 0.000 | 0.052 / 0.042 | +0.05 |
| PGA (g) | 0.188 / 0.182 | 0.203 / 0.217 | -0.12 |
| freeze-thaw days | 84.667 / 72.600 | -inf / -inf | +nan |

| ek ölçüm | değer |
|---|---|
| vaka: transit dose = 0 / = 1 payi | %42.0 / %30.0 |
| vaka: source-side dose SD | 0.447 |
| kontrol: transit dose = 0 / = 1 payi | %29.2 / %48.2 |
| kontrol: source-side dose SD | 0.430 |
| track payi (kontrol / M1 vakasi) | %31.5 / %6.5 |

## Katsayilar (kumelenmis SE, 50 km)

| model | sonuc |
|---|---|
| M1 kesif · doz_gecis | -1.1967 [-1.896, -0.497] OR 0.302 p=0.0008 |
| M1 kesif · doz_ust | +0.0999 [-0.656, +0.856] OR 1.105 p=0.7956 |
| M1 dogrulama · doz_gecis | -1.0149 [-2.474, +0.444] OR 0.362 p=0.1727 |
| M1 dogrulama · doz_ust | -0.1046 [-1.257, +1.047] OR 0.901 p=0.8587 |
| M2 kesif · doz_gecis | -0.8205 [-1.394, -0.247] OR 0.440 p=0.0051 |
| M2 kesif · doz_ust | +0.0911 [-0.500, +0.683] OR 1.095 p=0.7627 |
| M2 dogrulama · doz_gecis | -0.7999 [-1.597, -0.002] OR 0.449 p=0.0493 |
| M2 dogrulama · doz_ust | +0.2293 [-0.542, +1.000] OR 1.258 p=0.5599 |
