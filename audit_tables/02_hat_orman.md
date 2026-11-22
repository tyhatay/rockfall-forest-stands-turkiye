# Adım 3.2 — hat boyunca orman örtüsü ve kapalılık

Üretim: `01_kod/04_flowpy/02_hat_orman.py`  
Nokta: **3,255**, hat örneği: **232,288**  
Örnekleme aralığı: 25 m (5–80 örnek)

> **Ana doz değişkeni `hat_kapalilik_agirlikli`.** Hat boyunca eşit
> aralıklı örneklenen her noktada tepe kapalılığı; **orman olmayan**
> örnek **%0** sayılıyor. Açık arazi eksik veri değil, *engel yok*
> demektir. Noktasal kapalılık yalnızca %34'te doluydu (`data.md`
> 6.4k); bu değişken her örneği olan noktada tanımlı.

## 1. Kapsama

| Seçim | Hattı olan nokta | Örnek medyanı | Poligon eşleşen örnek |
|---|---|---|---|
| `en_dik` | 2,464 | 19 | %99.9 |
| `en_yuksek` | 2,464 | 38 | %99.9 |
| `en_uzak` | 2,464 | 41 | %99.9 |

## 2. Hat boyu orman — dağılım

| Seçim | Orman oranı medyan | >0 olan nokta | Ağırlıklı kapalılık medyan |
|---|---|---|---|
| `en_dik` | 0.306 | 1,554 | 2.58% |
| `en_yuksek` | 0.390 | 1,769 | 4.00% |
| `en_uzak` | 0.359 | 1,776 | 4.02% |

## 3. Kaynağın örtüsü — “çıplak kaynak” tasarımının örneklemi

Noktada ölçülen `nokta_kayalik` yalnızca **20** vaka veriyordu; ama
tasarım **kaynağın** kayalık olmasını istiyor, kaynak yukarıda.

| Seçim | Kaynak orman | Kaynak kayalık (ARZ=17) | Kaynak poligonsuz |
|---|---|---|---|
| `en_dik` | 1,364 | **74** | 794 |
| `en_yuksek` | 1,426 | **64** | 794 |
| `en_uzak` | 1,447 | **57** | 794 |

## 4. Kaynak `ARZ_KUL` dağılımı (`en_dik`)

| ARZ_KUL | n |
|---|---|
| 1 | 1,305 |
| 14 | 287 |
| 107 | 202 |
| 12 | 180 |
| 103 | 107 |
| 17 | 74 |
| 15 | 62 |
| 2 | 59 |
| 108 | 53 |
| 110 | 44 |

---

**Sonraki adım:** `03_beta_testi.py` — H2a: β ~ `hat_kapalilik_agirlikli`, üç kaynak seçiminde ayrı, şekil testi
(karesel + spline) ile birlikte.
