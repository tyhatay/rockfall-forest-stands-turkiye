# Adım 3.5 — destekleyici analizler ve tahsis boşluğu

Üretim: `01_kod/04_flowpy/05_destekleyici.py`  
H2a örneklemi: n = **425**  
Temel etki: **+2.9637** (SE 0.9057, n 425)

> **Güç kuralı, sonuçtan önce yazıldı.** Alt örneklemde beklenen
> SE ≈ 0.9057 × √(425/n). Aynı etki büyüklüğünde
> p < 0,05 için n ≳ 160 gerekiyor. **n < 120** olan bir
> alt örneklemde çıkan null, etkinin yokluğu **değil** gücün
> yokluğudur.

## A. Çıplak kaynak tasarımı — ÖRNEKLEM YETERSİZ

Kaynağı yapısal olarak ağaçsız olan olaylar. H2a örneklemi
**aynı zamanda** hat boyunca orman istiyor; kesişim:

| Kaynak ölçütü | n | beklenen SE | beklenen p | durum |
|---|---|---|---|---|
| 17 kayalik | **8** | 6.60 | 0.653 | **YETERSİZ** |
| 17+14 kayalik+tasli | **26** | 3.66 | 0.418 | **YETERSİZ** |
| 17+14+15 (+erozyonlu) | **29** | 3.47 | 0.393 | **YETERSİZ** |
| 17+14+15+12 (+OT agacsiz) | **32** | 3.30 | 0.369 | **YETERSİZ** |

**Sonuç: yapılamıyor.** En geniş ölçütte bile n = 32; aynı
etki büyüklüğünde beklenen p > 0,05. Koşulsa çıkacak null
yorumlanamazdı. `metodoloji.md`'nin ikinci bağışık tasarımı
**düşüyor** — Adım 4 ve H3 ile aynı sebeple (`data.md` 6.1i).

## B. Muhafaza ormanı örtüşmesi — ÖRTÜŞME YOK

* Muhafaza ormanı **içinde**: **0** / 3,255
* En yakın muhafaza ormanına uzaklık: medyan **36.3 km**
* 2 km içinde: **10**

**Sonuç: yapılamıyor.** `GEN_KORUMA_ORMAN`'ın 318 poligonu ile
kayıtlı kaya düşmesi olayları arasında örtüşme yok. Bu başlı
başına bir **tahsis bulgusu** (bkz. C).

## C. Koruma fonksiyonu tahsisi — hat boyunca ölçüldü

| Ölçüm | n |
|---|---|
| hat hesaplanan nokta | 2,464 |
| ormanlı yörünge (örtü > 0) | 1,554 |
| örtü ≥ %50 | 915 |
| **2212 tahsisi hatta olan** | 5 |
| 2213 tahsisi hatta olan | 812 |
| **örtü ≥ %50 VE 2212 tahsisi YOK** | 912 |

**Bulgu.** OGM 493 poligon / 3.170 ha alanı FONK **2212 — Taş ve
Kaya Yuvarlanmayı Önleme** olarak tahsis etmiş
(`04_kod_listeleri/ogm_kodlari.md`). Yörüngesi hesaplanabilen
2,464 kaya düşmesi olayından yalnızca
**5** tanesinde blok böyle bir ormanın
altından geçmiş. Buna karşılık
**912** olayda blok
yörüngesinin en az yarısını ormanın altında geçirmiş ve o ormanın
**hiçbir kaya düşmesi koruma tahsisi yok.**

`ogm_kodlari.md`'de öngörülen **eksik tahsis** durumu ölçülmüş
oldu. Bu, makalenin uygulamaya dönük katkısı.

### C2. 2213 alt grubu — fark İDDİA EDİLEMEZ

| Alt grup | n | katsayı | SE | p |
|---|---|---|---|---|
| 2213 hatta VAR | 195 | +1.4508 | 1.0338 | 0.1605 |
| 2213 hatta YOK | 230 | +4.9466 | 1.3721 | 0.0003 |

**Formal etkileşim testi** (alt grupları ayrı koşmak yerine):

* `orman_orani × 2213` katsayısı: **-2.6863**, SE 1.4145, **p = 0.0575**
* %95 GA: **[-5.4587, +0.0860]** — sıfıra dokunuyor

**Sonuç: alt grup farkı iddia edilemez.** Alt gruplar ayrı
koşulduğunda fark büyük görünüyor (+1,45 vs +4,95) ama formal
etkileşim testi sınırda ve güven aralığı sıfırı içeriyor. Ayrıca
gruplar dengeli değil (doz medyanı %15,0 vs %8,7; yükseklik 962 vs
846 m). Alt grup ayrımı **betimsel** olarak raporlanacak, bir etki
farkı olarak değil.

---

**Özet.** İki destekleyici tasarım örneklem yetersizliğinden düştü
(A: n ≤ 32, B: örtüşme yok). Üçüncüsü bir **tahsis boşluğu bulgusu**
üretti ve bu, H2a'nın kendisinden bağımsız biçimde betimsel.
