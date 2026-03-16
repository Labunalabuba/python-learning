print("=" * 50)
print("DOSYA ISLEMLERI (FILE I/O)")
print("=" * 50)

print("\n1. DOSYA YAZMA:")

dosya = open("ornekler.txt", "w")
dosya.write("Merhaba Dunya\n")
dosya.write("Python Ogrenmesi\n")
dosya.write("Fintech Uygulamasi\n")
dosya.close()

print("ornekler.txt olusturuldu")

print("\n2. DOSYA OKUMA:")

dosya = open("ornekler.txt", "r")
icerik = dosya.read()
dosya.close()

print("Dosya icerigi:")
print(icerik)

print("\n3. SATIR SATIR OKUMA:")

dosya = open("ornekler.txt", "r")
satirlar = dosya.readlines()
dosya.close()

print("Satirlar:")
for i, satir in enumerate(satirlar, 1):
    print(str(i) + ". " + satir.strip())

print("\n4. WITH KULLANMA:")

with open("ornekler.txt", "r") as dosya:
    icerik = dosya.read()
    print("With ile okundu:")
    print(icerik)

print("\n5. APPEND MODU:")

with open("ornekler.txt", "a") as dosya:
    dosya.write("Yeni Satir Eklendi\n")

print("Yeni satir eklendi")

print("\n6. DOSYA SILME:")

import os
if os.path.exists("silinecek.txt"):
    os.remove("silinecek.txt")
    print("Dosya silindi")
else:
    print("Dosya bulunamadi")

print("\n" + "=" * 50)
print("JSON ISLEMLERI")
print("=" * 50)

print("\n1. JSON YAZMA:")

import json

hesaplar = {
    "hesap1": {
        "ad": "Ahmet",
        "bakiye": 5000,
        "iban": "TR001"
    },
    "hesap2": {
        "ad": "Fatma",
        "bakiye": 10000,
        "iban": "TR002"
    }
}

with open("hesaplar.json", "w") as dosya:
    json.dump(hesaplar, dosya, indent=2)

print("hesaplar.json olusturuldu")

print("\n2. JSON OKUMA:")

with open("hesaplar.json", "r") as dosya:
    veriler = json.load(dosya)

print("JSON verileri:")
for key in veriler:
    hesap = veriler[key]
    print("Ad: " + hesap["ad"])
    print("Bakiye: " + str(hesap["bakiye"]))

print("\n3. JSON PARSE:")

json_str = '{"musteri":"Ali", "bakiye":7500}'
veri = json.loads(json_str)

print("Musteri: " + veri["musteri"])
print("Bakiye: " + str(veri["bakiye"]))

print("\n4. PYTHON OBJESINI JSON YAP:")

class Hesap:
    def __init__(self, ad, bakiye):
        self.ad = ad
        self.bakiye = bakiye

h = Hesap("Ali", 5000)

hesap_dict = {
    "ad": h.ad,
    "bakiye": h.bakiye
}

json_str = json.dumps(hesap_dict)
print("JSON String: " + json_str)

print("\n" + "=" * 50)
print("CSV ISLEMLERI")
print("=" * 50)

print("\n1. CSV YAZMA:")

import csv

musteriler = [
    ["Ad", "Bakiye", "IBAN"],
    ["Ahmet", "5000", "TR001"],
    ["Fatma", "10000", "TR002"],
    ["Ali", "7500", "TR003"]
]

with open("musteriler.csv", "w") as dosya:
    yazar = csv.writer(dosya)
    yazar.writerows(musteriler)

print("musteriler.csv olusturuldu")

print("\n2. CSV OKUMA:")

with open("musteriler.csv", "r") as dosya:
    okuyucu = csv.reader(dosya)
    for satir in okuyucu:
        print(" - ".join(satir))

print("\n3. CSV DICTREADER:")

with open("musteriler.csv", "r") as dosya:
    okuyucu = csv.DictReader(dosya)
    for satir in okuyucu:
        print("Ad: " + satir["Ad"])
        print("Bakiye: " + satir["Bakiye"])

print("\n" + "=" * 50)
print("FINTECH ORNEKLERI")
print("=" * 50)

print("\n1. MUSTERI KAYDI:")

musteriler_veri = {
    "musteriler": [
        {
            "id": 1,
            "ad": "Ahmet Yilmaz",
            "bakiye": 5000
        },
        {
            "id": 2,
            "ad": "Fatma Kaya",
            "bakiye": 10000
        }
    ]
}

with open("musteriler_db.json", "w") as f:
    json.dump(musteriler_veri, f, indent=2)

print("Musteri veritabani kaydedildi")

print("\n2. ISLEM GECMISI:")

islemler = [
    ["Tarih", "Gonderici", "Alici", "Miktar"],
    ["2024-03-01", "Ahmet", "Fatma", "1000"],
    ["2024-03-02", "Fatma", "Ali", "500"],
    ["2024-03-03", "Ali", "Ahmet", "2000"]
]

with open("islem_gecmisi.csv", "w") as f:
    yazar = csv.writer(f)
    yazar.writerows(islemler)

print("Islem gecmisi kaydedildi")

print("\n3. KREDI KAYDI:")

krediler = {
    "krediler": [
        {
            "id": 1,
            "musteri": "Ahmet",
            "miktar": 10000,
            "oran": 0.15
        },
        {
            "id": 2,
            "musteri": "Fatma",
            "miktar": 50000,
            "oran": 0.10
        }
    ]
}

with open("krediler_db.json", "w") as f:
    json.dump(krediler, f, indent=2)

print("Kredi veritabani kaydedildi")

print("\n4. OKUMA VE ISLEM:")

with open("musteriler_db.json", "r") as f:
    data = json.load(f)

print("Tum Musteriler:")
for m in data["musteriler"]:
    print("- " + m["ad"] + " (" + str(m["bakiye"]) + ")")

print("\n5. CSV ISLE:")

toplam = 0
with open("musteriler.csv", "r") as f:
    okuyucu = csv.DictReader(f)
    for satir in okuyucu:
        toplam += int(satir["Bakiye"])

print("Toplam Bakiye: " + str(toplam))

print("\n" + "=" * 50)
print("OZET")
print("=" * 50)
print("- open(): Dosya ac")
print("- read(): Oku")
print("- write(): Yaz")
print("- json.dump(): JSON yaz")
print("- json.load(): JSON oku")
print("- csv.writer(): CSV yaz")
print("- csv.reader(): CSV oku")
