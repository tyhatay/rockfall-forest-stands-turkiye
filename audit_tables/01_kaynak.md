# Adım 3.1 — kaynak alanı ve enerji çizgisi geometrisi

Üretim: `01_kod/04_flowpy/01_kaynak.py`  
Nokta: **3,255** (alt küme `model_dar_tam`)  
Kaynak ölçütü: yukarıda + eğim > 35° + dh ≥ 10 m

> **`beta_maks` neden yetmiyordu.** Adım 1.1'in `beta_maks_1000m`'i
> yukarıdaki *her* hücreye açının maksimumu — bir topoğrafya
> tanımlayıcısı. Bloğun nereden geldiğini ve ne kadar yol aldığını
> kodlamıyor, bu yüzden enerji sönümlenmesini ölçemez. Ölçüldü:
> `beta_maks` ile tepe kapalılığı arasında eğilim yok (`data.md` 6.5a).

> **Üç kaynak seçimi, keyfi seçim yok.** Gerçek kopma noktası
> bilinmiyor (AFAD kaydı çarpma noktası). `en_dik` = argmax β (en az
> varsayım, β'nın üst sınırı), `en_yuksek` = argmax Δh, `en_uzak` =
> argmax L (β'nın alt sınırı). H2a üçünde ayrı koşacak.

## 1. Kaynak bulunma oranı

| Yarıçap | Nitelikli kaynak var | % | Nitelikli hücre medyanı |
|---|---|---|---|
| 1000m | 2,464 | 75.7% | 114 |
| 2000m | 2,837 | 87.2% | 375 |

## 2. Seçime göre β dağılımı

| Yarıçap | Seçim | n | β medyan | β ort. | β sd | β ≥ 28° |
|---|---|---|---|---|---|---|
| 1000m | `en_dik` | 2,464 | 20.14 | 20.86 | 11.00 | 662 |
| 1000m | `en_yuksek` | 2,464 | 15.06 | 15.62 | 7.70 | 159 |
| 1000m | `en_uzak` | 2,464 | 7.02 | 8.23 | 5.87 | 10 |
| 2000m | `en_dik` | 2,837 | 18.69 | 19.51 | 11.16 | 675 |
| 2000m | `en_yuksek` | 2,837 | 11.95 | 12.54 | 6.56 | 51 |
| 2000m | `en_uzak` | 2,837 | 4.60 | 5.77 | 4.68 | 0 |

## 3. Geometri: Δh ve L

| Yarıçap | Seçim | Δh medyan (m) | L medyan (m) |
|---|---|---|---|
| 1000m | `en_dik` | 126 | 460 |
| 1000m | `en_yuksek` | 217 | 924 |
| 1000m | `en_uzak` | 115 | 997 |
| 2000m | `en_dik` | 152 | 619 |
| 2000m | `en_yuksek` | 348 | 1818 |
| 2000m | `en_uzak` | 150 | 1998 |

## 4. `beta_maks` ile karşılaştırma (gerileme kontrolü)

`en_dik_beta` ≤ `beta_maks` olmalı: aynı maksimum ama kaynak ölçütüyle
kısıtlanmış. Büyük çıkarsa bir hata var.

* ikisi dolu: **2,464**
* `en_dik_beta_1000m` > `beta_maks_1000m` ihlali: **0**  ✅
* medyan fark (`beta_maks` − `en_dik`): **2.47°**

---

**Sonraki adım:** `02_hat_orman.py` — kaynak→nokta doğrusu boyunca
orman örtüsü ve tepe kapalılığı örneklenecek. H2a'nın doz değişkeni
nokta kapalılığı değil **hat boyu ortalama kapalılık** olacak; bu hem
mekanizma açısından doğru hem örneklemi büyütüyor (sürekli ortalama,
seyrek kategorik yerine).
