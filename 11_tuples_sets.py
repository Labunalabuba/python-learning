# TUPLE'LAR VE KÜMELER (TUPLES & SETS)

print("=" * 60)
print("TUPLE'LAR (TUPLES)")
print("=" * 60)

print("\n1. Tuple Olusturma:")
banka_kodlari = ("Ziraat", "Is", "Garanti")
print(f"Tuple: {banka_kodlari}")
print(f"Tip: {type(banka_kodlari)}")
print(f"Uzunluk: {len(banka_kodlari)}")

print("\n2. Tuple Erişimi:")
print(f"Ilk: {banka_kodlari[0]}")
print(f"Son: {banka_kodlari[-1]}")
print(f"Dilim: {banka_kodlari[0:2]}")

print("\n3. Tuple vs Liste:")
liste = [1, 2, 3]
tuple_ = (1, 2, 3)

print(f"Liste degistirilebilir:")
liste[0] = 999
print(f"  {liste}")

print(f"Tuple degistirilemez:")
try:
    tuple_[0] = 999
except TypeError as e:
    print(f"  Hata: {e}")

print("\n4. Tek Elemanli Tuple:")
tek = (42,)
print(f"Tek eleman tuple: {tek}")
print(f"Tip: {type(tek)}")

print("\n5. Tuple Dongusu:")
koordinatlar = [(10, 20), (30, 40), (50, 60)]
for x, y in koordinatlar:
    print(f"X: {x}, Y: {y}")

print("\n6. Tuple Metodlari:")
sayilar = (1, 2, 3, 2, 4, 2)
print(f"Tuple: {sayilar}")
print(f"2 kac kez: {sayilar.count(2)}")
print(f"3 nerede: {sayilar.index(3)}")

print("\n7. Tuple Unpacking:")
hesap = ("Ahmet", 5000, "Vadesiz")
ad, bakiye, tip = hesap
print(f"Ad: {ad}")
print(f"Bakiye: {bakiye}")
print(f"Tip: {tip}")

print("\n" + "=" * 60)
print("KÜMELER (SETS)")
print("=" * 60)

print("\n1. Kume Olusturma:")
banka_listesi = {"Ziraat", "Is", "Garanti", "Akbank"}
print(f"Kume: {banka_listesi}")
print(f"Tip: {type(banka_listesi)}")

print("\n2. Kume Ozellikleri:")
print(f"Uzunluk: {len(banka_listesi)}")
print(f"Sirali degil:")
kume1 = {3, 1, 2}
kume2 = {1, 2, 3}
print(f"  {kume1} == {kume2}: {kume1 == kume2}")

print("\n3. Kopya Yok (Unique):")
sayilar = [1, 2, 2, 3, 3, 3, 4]
benzersiz = set(sayilar)
print(f"Liste: {sayilar}")
print(f"Kume: {benzersiz}")

print("\n4. Kume Islemleri:")
kume_a = {1, 2, 3, 4}
kume_b = {3, 4, 5, 6}

print(f"A: {kume_a}")
print(f"B: {kume_b}")
print(f"Birlesim (union): {kume_a | kume_b}")
print(f"Kesisim (intersection): {kume_a & kume_b}")
print(f"Fark: {kume_a - kume_b}")
print(f"Simetrik Fark: {kume_a ^ kume_b}")

print("\n5. Kume Metodlari:")
bankalar = {"Ziraat", "Is"}
print(f"Orijinal: {bankalar}")

bankalar.add("Garanti")
print(f"Add: {bankalar}")

bankalar.update(["Akbank", "Deniz"])
print(f"Update: {bankalar}")

bankalar.remove("Ziraat")
print(f"Remove: {bankalar}")

print("\n6. Kume Dongusu:")
musteriler = {"Ahmet", "Fatma", "Ali"}
print("Musteriler:")
for musteri in musteriler:
    print(f"  - {musteri}")

print("\n" + "=" * 60)
print("FINTECH UYGULAMALARI")
print("=" * 60)

print("\n1. Hesap Numaralari (Tuple):")
hesap_bilgileri = {
    "Ahmet": ("TR123", "Vadesiz", 5000),
    "Fatma": ("TR456", "Vadeli", 10000)
}

for musteri, (iban, tip, bakiye) in hesap_bilgileri.items():
    print(f"{musteri}: {iban} ({tip}) - {bakiye} TL")

print("\n2. Benzersiz Musteriler (Set):")
islem_musterileri = ["Ahmet", "Fatma", "Ahmet", "Ali", "Fatma"]
benzersiz_musteriler = set(islem_musterileri)
print(f"Islem yapan: {islem_musterileri}")
print(f"Benzersiz: {benzersiz_musteriler}")
print(f"Sayi: {len(benzersiz_musteriler)}")

print("\n3. Banka Kodlari (Set):")
kodlar_a = {"001", "002", "003"}
kodlar_b = {"003", "004", "005"}

print(f"Banka A kodlari: {kodlar_a}")
print(f"Banka B kodlari: {kodlar_b}")
print(f"Ortak kodlar: {kodlar_a & kodlar_b}")
print(f"Farkli kodlar: {kodlar_a | kodlar_b}")

print("\n4. Yasakli Isimler (Set):")
yasakli = {"admin", "root", "system"}
kullanicilar = ["admin", "fatma", "ali", "root"]

print(f"Yasakli: {yasakli}")
print(f"Giris yapanlar: {kullanicilar}")

yasakli_kullanicilar = set(kullanicilar) & yasakli
izin_verilen = set(kullanicilar) - yasakli

print(f"Yasakli kullanicilar: {yasakli_kullanicilar}")
print(f"Izin verilen: {izin_verilen}")

print("\n5. Koordinatlar (Tuple Liste):")
subenler = [
    ("Istanbul", 41.0082, 28.9784),
    ("Ankara", 39.9334, 32.8597),
    ("Izmir", 38.4161, 27.1330)
]

print("Subekeler:")
for sube, lat, long in subenler:
    print(f"  {sube}: ({lat}, {long})")

print("\n6. Islem Tipleri (Set):")
islem_tipi_a = {"Transfer", "Yatirma", "Cekme"}
islem_tipi_b = {"Transfer", "Odeme", "Kredi"}

ortaklar = islem_tipi_a & islem_tipi_b
farklilar = islem_tipi_a ^ islem_tipi_b

print(f"A Bankas? islemler: {islem_tipi_a}")
print(f"B Bankas? islemler: {islem_tipi_b}")
print(f"Ortak islemler: {ortaklar}")
print(f"Sadece biri var: {farklilar}")
