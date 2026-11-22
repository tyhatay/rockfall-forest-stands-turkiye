# 28 — tekrar kayitlar ve kisa yol dozu

## Betimleme

| olcum | deger |
|---|---|
| vaka | 343 |
| tam ayni koordinat (konum_grup_n > 1) | 0 |
| 50 m: konum kumesi | 316 (>1 kayitli 14, o kumelerde 41 kayit, en buyuk 9) |
| 250 m: konum kumesi | 297 (>1 kayitli 29, o kumelerde 75 kayit, en buyuk 9) |
| 500 m: konum kumesi | 291 (>1 kayitli 34, o kumelerde 86 kayit, en buyuk 9) |
| 250 m kumesi icinde AYNI TARIHLI fazla kayit | 12 |
| kontrol 250 m: kume / >1 kayitli / en buyuk | 3748 / 78 / 4 |
| vaka: doz_gecis_n medyan / n=2 payi / n<3 payi | 6 / %14.3 / %14.3 |
| kontrol: doz_gecis_n medyan / n=2 payi / n<3 payi | 6 / %16.7 / %16.7 |
| doz_kuyruksuz_n en buyuk (ust sinir 80 bagliyor mu?) | 38 |

## M1 duyarlilik (kesif dilimi)

| sürüm | n | vaka | doz_gecis | %95 GA | OR | p |
|---|---|---|---|---|---|---|
| referans (tum vakalar) | 3,395 | 159 | -1.1967 | [-1.896, -0.497] | 0.302 | 0.0008 |
| 250 m kume basina tek vaka | 3,376 | 140 | -1.2579 | [-1.926, -0.590] | 0.284 | 0.0002 |
| 500 m kume basina tek vaka | 3,372 | 136 | -1.2055 | [-1.847, -0.564] | 0.300 | 0.0002 |
| 250 m agirlik 1/kume (GLM) | 3,395 | 159 | -1.2028 | [-1.870, -0.536] | 0.300 | 0.0004 |
| 250 m tek nokta, IKI GRUPTA | 3,302 | 140 | -1.2787 | [-1.947, -0.611] | 0.278 | 0.0002 |
| gecis penceresi >= 3 ornek | 2,833 | 141 | -1.3293 | [-2.103, -0.556] | 0.265 | 0.0008 |
| gecis penceresi >= 5 ornek | 2,054 | 90 | -1.5698 | [-2.514, -0.626] | 0.208 | 0.0011 |
