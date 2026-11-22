# Adım 3.3 — H2a ana test: β ~ hat boyu kapalılık dozu

Üretim: `01_kod/04_flowpy/03_beta_testi.py`  
β eşiği: **28°**, yarıçap 1000m, küme hücresi 50 km

> **Yapısal bağışıklık.** Örneklem, hat boyunca **ormanı olan**
> noktalarla sınırlı. Karşılaştırılan bütün birimlerin yörüngesinde
> orman var, dolayısıyla "burada ağaç yetişmez" bir **gradyanı**
> açıklayamaz (`metodoloji.md` H2a).

> **Δh kontrol EDİLİYOR, L edilmiyor.** β = atan(Δh/L). Δh düşüş
> yüksekliği — ormanın nedeni olmadığı bir tasarım özelliği, meşru
> kontrol. L ise **koşu mesafesi**, yani sonucun kendisi: kontrol
> edilemez, ama bağımlı değişken olabilir. Kontrolsüz ilk belirtim
> mekanik bir tuzak üretiyordu (`data.md` 6.5g). Kod bunu
> `kontrol_sizinti()` ile zorluyor.

## `en_dik` — n = 321

Küme sayısı: 84, R² = 0.4080

| Terim | Katsayı | SE (kümelenmiş) | p | SE (HC3) | p (HC3) |
|---|---|---|---|---|---|
| `doz` | +0.02337 | 0.01248 | 0.0611 | 0.01264 | 0.0644 |
| `logdh` | -3.03261 | 0.35436 | 0.0000 | 0.40413 | 0.0000 |
| `yukseklik_m` | -0.00011 | 0.00089 | 0.8988 | 0.00091 | 0.9007 |

Dozun %5–%95 aralığı (81.6 puan) üzerindeki etki: **+1.91°**

### Doz dörtte-birlerine göre β (betimsel)

| Doz dilimi | n | β ortalama | β medyan |
|---|---|---|---|
| (0.378, 4.4] | 89 | 33.76 | 32.04 |
| (4.4, 9.794] | 72 | 34.86 | 32.99 |
| (9.794, 41.529] | 80 | 35.68 | 34.15 |
| (41.529, 85.5] | 80 | 35.74 | 34.04 |

## `en_yuksek` — n = 119

Küme sayısı: 47, R² = 0.2798

| Terim | Katsayı | SE (kümelenmiş) | p | SE (HC3) | p (HC3) |
|---|---|---|---|---|---|
| `doz` | -0.04435 | 0.01450 | 0.0022 | 0.01527 | 0.0037 |
| `logdh` | -1.30538 | 0.97157 | 0.1791 | 0.94224 | 0.1659 |
| `yukseklik_m` | -0.00089 | 0.00105 | 0.3963 | 0.00110 | 0.4200 |

Dozun %5–%95 aralığı (63.4 puan) üzerindeki etki: **-2.81°**

## Özet — bütün seçimler ve modeller

| Seçim | Model | Terim | n | Katsayı | SE (küme) | p |
|---|---|---|---|---|---|---|
| `en_dik` | dh_kontrolsuz | `doz` | 321 | +0.04087 | 0.01371 | 0.0029 |
| `en_dik` | dh_kontrolsuz | `yukseklik_m` | 321 | -0.00167 | 0.00093 | 0.0727 |
| `en_dik` | BIRINCIL_dh_kontrollu | `doz` | 321 | +0.02337 | 0.01248 | 0.0611 |
| `en_dik` | BIRINCIL_dh_kontrollu | `logdh` | 321 | -3.03261 | 0.35436 | 0.0000 |
| `en_dik` | BIRINCIL_dh_kontrollu | `yukseklik_m` | 321 | -0.00011 | 0.00089 | 0.8988 |
| `en_dik` | karesel | `doz` | 321 | +0.03327 | 0.03968 | 0.4017 |
| `en_dik` | karesel | `doz_kare` | 321 | -0.00013 | 0.00050 | 0.7906 |
| `en_dik` | karesel | `logdh` | 321 | -3.03960 | 0.36181 | 0.0000 |
| `en_dik` | karesel | `yukseklik_m` | 321 | -0.00009 | 0.00089 | 0.9171 |
| `en_dik` | dilim | `doz_Q_(4.4, 9.794]` | 321 | +0.47536 | 0.66749 | 0.4764 |
| `en_dik` | dilim | `doz_Q_(9.794, 41.529]` | 321 | +1.78006 | 0.77906 | 0.0223 |
| `en_dik` | dilim | `doz_Q_(41.529, 85.5]` | 321 | +1.48221 | 0.84663 | 0.0800 |
| `en_dik` | dilim | `logdh` | 321 | -3.08614 | 0.34472 | 0.0000 |
| `en_dik` | dilim | `yukseklik_m` | 321 | +0.00002 | 0.00094 | 0.9821 |
| `en_dik` | kosu_mesafesi | `doz` | 321 | -0.00087 | 0.00046 | 0.0574 |
| `en_dik` | kosu_mesafesi | `logdh` | 321 | +1.11093 | 0.01292 | 0.0000 |
| `en_dik` | kosu_mesafesi | `yukseklik_m` | 321 | +0.00000 | 0.00003 | 0.8954 |
| `en_yuksek` | dh_kontrolsuz | `doz` | 119 | -0.03970 | 0.01300 | 0.0022 |
| `en_yuksek` | dh_kontrolsuz | `yukseklik_m` | 119 | -0.00094 | 0.00111 | 0.3999 |
| `en_yuksek` | BIRINCIL_dh_kontrollu | `doz` | 119 | -0.04435 | 0.01450 | 0.0022 |
| `en_yuksek` | BIRINCIL_dh_kontrollu | `logdh` | 119 | -1.30538 | 0.97157 | 0.1791 |
| `en_yuksek` | BIRINCIL_dh_kontrollu | `yukseklik_m` | 119 | -0.00089 | 0.00105 | 0.3963 |
| `en_yuksek` | karesel | `doz` | 119 | +0.00601 | 0.04122 | 0.8840 |
| `en_yuksek` | karesel | `doz_kare` | 119 | -0.00070 | 0.00043 | 0.1024 |
| `en_yuksek` | karesel | `logdh` | 119 | -1.27336 | 0.96613 | 0.1875 |
| `en_yuksek` | karesel | `yukseklik_m` | 119 | -0.00073 | 0.00108 | 0.5012 |
| `en_yuksek` | dilim | `doz_Q_(4.279, 25.5]` | 119 | +0.98000 | 1.27934 | 0.4437 |
| `en_yuksek` | dilim | `doz_Q_(25.5, 49.62]` | 119 | -1.01271 | 1.01110 | 0.3165 |
| `en_yuksek` | dilim | `doz_Q_(49.62, 85.5]` | 119 | -2.08013 | 1.08747 | 0.0558 |
| `en_yuksek` | dilim | `logdh` | 119 | -0.92865 | 1.05560 | 0.3790 |
| `en_yuksek` | dilim | `yukseklik_m` | 119 | -0.00062 | 0.00104 | 0.5490 |
| `en_yuksek` | kosu_mesafesi | `doz` | 119 | +0.00168 | 0.00055 | 0.0021 |
| `en_yuksek` | kosu_mesafesi | `logdh` | 119 | +1.04880 | 0.03688 | 0.0000 |
| `en_yuksek` | kosu_mesafesi | `yukseklik_m` | 119 | +0.00003 | 0.00004 | 0.4277 |

---

**Yorum sınırı.** Bu bir ilişki ölçümü; nedensellik iddia edilmiyor.
Ters nedensellik kanalı yapısal bağışıklıkla daraltıldı ama
kaldırılmadı. Noktalar çarpma noktası, kaynak tahmin edilmiş
(`data.md` 6.5b, üç seçim duyarlılık ekseni).
