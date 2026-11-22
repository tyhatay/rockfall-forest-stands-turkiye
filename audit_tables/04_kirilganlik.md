# Adım 3.4 — H2a kırılganlık teşhisi

Üretim: `01_kod/04_flowpy/04_kirilganlik.py`  
Birincil belirtim: `β ~ doz + log Δh + kontroller`, 50 km kümelenmiş SE

## A. Eşik taraması — güç kaybı mı yapısal mı?

| β eşiği | n | küme | doz katsayısı | SE | p | t |
|---|---|---|---|---|---|---|
| 26 | 520 | 121 | +0.02628 | 0.01091 | 0.0160 | +2.41 |
| 27 | 465 | 112 | +0.02500 | 0.01071 | 0.0196 | +2.33 |
| 28 | 425 | 111 | +0.02403 | 0.01030 | 0.0197 | +2.33 |
| 29 | 375 | 102 | +0.01744 | 0.01106 | 0.1147 | +1.58 |
| 30 | 343 | 96 | +0.01663 | 0.01069 | 0.1198 | +1.56 |
| 31 | 307 | 89 | +0.01772 | 0.00937 | 0.0585 | +1.89 |
| 32 | 275 | 84 | +0.01641 | 0.01065 | 0.1235 | +1.54 |

## B. Aynı örneklemde kaynak tanımı — en önemli test

`en_dik` n = 425, `en_yuksek` n = 137, **kesişim n = 114**

| Kaynak tanımı | Örneklem | n | doz katsayısı | SE | p |
|---|---|---|---|---|---|
| `en_dik` | kesisim | 114 | +0.03421 | 0.01301 | 0.0085 |
| `en_yuksek` | kesisim | 114 | -0.01106 | 0.01304 | 0.3962 |
| `en_dik` | kendi | 425 | +0.02403 | 0.01030 | 0.0197 |
| `en_yuksek` | kendi | 137 | -0.01012 | 0.01185 | 0.3933 |

## C. Etkili gözlem — jackknife ve küme bootstrap

* Temel katsayı: **+0.02403**
* Küme bırakmalı jackknife (111 küme): [+0.02065, +0.02832], medyan +0.02408
* İşaret değiştiren küme sayısı: **0** / 111
* Küme bootstrap (2000 tekrar) %95 GA: **[+0.00342, +0.04456]**
* Bootstrap dağılımında katsayı ≤ 0 olma oranı: **%1.8**

## D. Doz ayrıştırma — örtü oranı mı, kapalılık yoğunluğu mu?

| Doz değişkeni | katsayı | SE | p | R² |
|---|---|---|---|---|
| hat_kapalilik_agirlikli (birincil) | +0.02403 | 0.01030 | 0.0197 | 0.484 |
| hat_orman_orani (yalnizca ortu) | +2.96369 | 0.90567 | 0.0011 | 0.493 |
| ormanli kisimdaki kapalilik | +0.00933 | 0.00850 | 0.2724 | 0.477 |
| ikisi birlikte -> ortu orani | +2.93855 | 0.89813 | 0.0011 | 0.495 |
| ikisi birlikte → kapalılık yoğunluğu | +0.00840 | 0.00833 | 0.3130 | 0.495 |

## E. Yarıçap — 1000 m vs 2000 m

| Yarıçap | n | küme | katsayı | SE | p |
|---|---|---|---|---|---|
| 1000m | 425 | 111 | +0.02403 | 0.01030 | 0.0197 |
| 2000m | 433 | 113 | +0.02279 | 0.01040 | 0.0285 |

## F. Sansür testi — kaynak tanımı yarıçapa mı bağlı?

Ölçüt: arama yarıçapı 2 katına çıkarılınca L medyanı ne kadar
artıyor? Fiziksel bir tanımda L **araziden** gelir, yarıçaptan
gelmez (≈1,0 kat). Yarıçapla orantılı artıyorsa (≈2,0 kat) tanım
**sansürlü** ve geçerli bir duyarlılık ekseni değildir.

| Seçim | L medyan 1 km | L medyan 2 km | kat | L/yarıçap | sınırda |
|---|---|---|---|---|---|
| `en_dik` | 460.5 m | 500.6 m | **1.09×** | 0.460 | 10.6% |
| `en_yuksek` | 923.8 m | 1825.8 m | **1.98×** | 0.924 | 41.4% |
| `en_uzak` | 997.1 m | 1998.7 m | **2.00×** | 0.997 | 80.0% |

## G. Örtü oranı dozuyla bütün eksenler

| Eksen | n | katsayı | SE | p |
|---|---|---|---|---|
| β eşiği 26 | 520 | +3.6819 | 0.8417 | 0.0000 |
| β eşiği 27 | 465 | +2.9212 | 0.9094 | 0.0013 |
| β eşiği 28 | 425 | +2.9637 | 0.9057 | 0.0011 |
| β eşiği 29 | 375 | +3.1096 | 0.8401 | 0.0002 |
| β eşiği 30 | 343 | +3.1126 | 0.7576 | 0.0000 |
| β eşiği 31 | 307 | +3.2375 | 0.7964 | 0.0000 |
| β eşiği 32 | 275 | +3.1259 | 0.9188 | 0.0007 |
| `en_dik` (kendi) | 425 | +2.9637 | 0.9057 | 0.0011 |
| `en_dik` (kesisim) | 114 | +3.2519 | 1.1788 | 0.0058 |
| `en_yuksek` (kendi) | 137 | +0.9765 | 0.9826 | 0.3204 |
| `en_yuksek` (kesisim) | 114 | +1.2910 | 1.1490 | 0.2612 |

