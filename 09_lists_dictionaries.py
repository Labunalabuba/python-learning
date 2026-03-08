# LİSTELER VE SÖZLÜKLER

print("=" * 50)
print("LISTELER (LISTS)")
print("=" * 50)

print("\n1. Liste Olusturma:")
bankalar = ["Ziraat", "Is Bankasi", "Garanti", "Akbank"]
print(f"Bankalar: {bankalar}")
print(f"Ilk banka: {bankalar[0]}")
print(f"Son banka: {bankalar[-1]}")

print("\n2. Liste Ozellikleri:")
sayilar = [10, 20, 30, 40, 50]
print(f"Uzunluk: {len(sayilar)}")
print(f"En buyuk: {max(sayilar)}")
print(f"En kucuk: {min(sayilar)}")
print(f"Toplam: {sum(sayilar)}")

print("\n3. Liste Metodlari:")
hesaplar = ["Vadesiz", "Vadeli"]
hesaplar.append("Tasarruf")
print(f"Eklendi: {hesaplar}")

hesaplar.insert(1, "Yatirim")
print(f"Eklendi (pozisyon 1): {hesaplar}")

hesaplar.remove("Tasarruf")
print(f"Cikarıldi: {hesaplar}")

print("\n4. Slicing (Dilim Alma):")
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Ilk 3: {sayilar[:3]}")
print(f"Son 3: {sayilar[-3:]}")
print(f"Ortadaki 4: {sayilar[3:7]}")
print(f"Her ikinci: {sayilar[::2]}")

print("\n5. Liste Dongusu:")
hesaplar = [
    {"ad": "Vadesiz", "faiz": 0.02},
    {"ad": "Vadeli", "faiz": 0.05},
    {"ad": "Tasarruf", "faiz": 0.03}
]
for hesap in hesaplar:
    print(f"{hesap['ad']}: %{hesap['faiz']*100}")

print("\n" + "=" * 50)
print("SOZLUKLER (DICTIONARIES)")
print("=" * 50)

print("\n1. Sozluk Olusturma:")
musteri = {
    "ad": "Ahmet",
    "yas": 35,
    "bakiye": 5000,
    "olusturulma": "2023-01-01"
}
print(f"Musteri: {musteri}")
print(f"Ad: {musteri['ad']}")
print(f"Bakiye: {musteri['bakiye']} TL")

print("\n2. Sozluk Metodlari:")
hesap = {"tip": "Vadesiz", "faiz": 0.02}
print(f"Anahtarlar: {hesap.keys()}")
print(f"Degerler: {hesap.values()}")
print(f"Tumlu: {hesap.items()}")

print("\n3. Sozluk Degistirme:")
musteri = {"ad": "Fatma", "yas": 28}
musteri["bakiye"] = 10000
print(f"Eklendi: {musteri}")

musteri["yas"] = 29
print(f"Guncellenen: {musteri}")

musteri.pop("yas")
print(f"Cikarıldi: {musteri}")

print("\n4. Sozluk Dongusu:")
hesap = {"tip": "Vadesiz", "faiz": 0.02, "vergi": 0.10}
for anahtar, deger in hesap.items():
    print(f"{anahtar}: {deger}")

print("\n" + "=" * 50)
print("FINTECH UYGULAMALARI")
print("=" * 50)

print("\n1. Musteri Veritabani:")
musteriler = [
    {"id": 1, "ad": "Ahmet", "bakiye": 5000, "kredi_skoru": 750},
    {"id": 2, "ad": "Fatma", "bakiye": 10000, "kredi_skoru": 680},
    {"id": 3, "ad": "Ali", "bakiye": 3000, "kredi_skoru": 620}
]

for musteri in musteriler:
    if musteri["kredi_skoru"] >= 700:
        durum = "VIP"
    else:
        durum = "Normal"
    print(f"{musteri['ad']} ({durum}): {musteri['bakiye']} TL")

print("\n2. Hesap Islemleri:")
hesap = {
    "hesap_no": "TR123",
    "bakiye": 5000,
    "islemler": [
        {"tip": "Yatirma", "tutar": 1000},
        {"tip": "Cekme", "tutar": -500},
        {"tip": "Transfer", "tutar": -200}
    ]
}

print(f"Hesap: {hesap['hesap_no']}")
print(f"Bakiye: {hesap['bakiye']} TL")
print("Islemler:")
for islem in hesap["islemler"]:
    print(f"  - {islem['tip']}: {islem['tutar']} TL")

print("\n3. Yatirim Portfoyü:")
portfoy = {
    "hisse": {"tutar": 50000, "kazanc": 0.15},
    "tahvil": {"tutar": 30000, "kazanc": 0.08},
    "altin": {"tutar": 20000, "kazanc": 0.05}
}

total_yatirim = 0
total_kazanc = 0

for yatirim, veri in portfoy.items():
    tutar = veri["tutar"]
    kazanc = tutar * veri["kazanc"]
    total_yatirim += tutar
    total_kazanc += kazanc
    print(f"{yatirim.capitalize()}: {tutar} TL (Kazanc: {kazanc:.2f} TL)")

print(f"Toplam Yatirim: {total_yatirim} TL")
print(f"Toplam Kazanc: {total_kazanc:.2f} TL")

print("\n4. List Comprehension:")
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cift_sayilar = [x for x in sayilar if x % 2 == 0]
kareler = [x**2 for x in sayilar]

print(f"Cift sayilar: {cift_sayilar}")
print(f"Kareler: {kareler}")

print("\n5. Dictionary Comprehension:")
faizler = {ay: 0.10 + (ay * 0.01) for ay in range(1, 6)}
print(f"Aylara gore faiz: {faizler}")
