# Adım 3.6 — hat boyunca tür bileşimi doz-yanıtı

Örneklem n = 425, küme 111; bileşim altkümesi n = 420.
Türü çözülen pay ormanlı örneklerde ortalama %99.1.

| Model | Terim | Katsayı | %95 GA | p | n |
|---|---|---|---|---|---|
| A taban | `orman_orani` | +1.6135 | [+0.259, +2.968] | 0.0195 | 425 |
| B ayristirma | `ibreli` | +1.3992 | [-0.284, +3.082] | 0.1032 | 425 |
| B ayristirma | `yaprakli` | +1.5383 | [-0.005, +3.082] | 0.0508 | 425 |
| B ayristirma | `karisik` | +1.8767 | [+0.185, +3.568] | 0.0297 | 425 |
| B ayristirma | `coz_yok` | +0.8967 | [-4.425, +6.219] | 0.7412 | 425 |
| B Wald | `ucu esit` | +0.3373 | — | 0.8448 | 425 |
| C bilesim | `orman_orani` | +1.5359 | [+0.166, +2.906] | 0.0280 | 420 |
| C bilesim | `ibreli_pay_c` | -0.1918 | [-1.062, +0.679] | 0.6660 | 420 |
| C2 kukla | `orman_orani` | +1.5391 | [+0.166, +2.912] | 0.0280 | 420 |
| C2 kukla | `ibreli_k_c` | -0.1409 | [-0.975, +0.693] | 0.7405 | 420 |
| D etkilesim | `etk` | +0.1114 | [-2.939, +3.162] | 0.9430 | 420 |
| TUZAK ayri: agirlikli ibreli | `orman_orani` | -0.9206 | [-3.872, +2.030] | 0.5409 | 91 |
| TUZAK ayri: agirlikli yaprakli | `orman_orani` | +1.8724 | [+0.384, +3.361] | 0.0137 | 329 |

**Sonuç.** Aynı örtü genişliğinde ibreli ve yapraklı yörüngeler ayırt edilemiyor. Düzey testi ana etki büyüklüğünde bir farkı saptayacak güçte; etkileşim testi değil (`data.md` 6.12).

**TUZAK satırları makaleye girmez** — gerekçe betiğin başında.
