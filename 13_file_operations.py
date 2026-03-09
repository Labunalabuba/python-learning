# DOSYA ISLEMLERI (FILE OPERATIONS)

import os

print("=" * 50)
print("DOSYA ISLEMLERI")
print("=" * 50)

print("\n1. DOSYA YAZMA:")
dosya = open("hesap.txt", "w")
dosya.write("Ahmet Yilmaz\n")
dosya.write("Bakiye: 5000 TL\n")
dosya.write("Hesap Tipi: Vadesiz\n")
dosya.close()
print("hesap.txt yazildi")

print("\n2. DOSYA OKUMA:")
dosya = open("hesap.txt", "r")
icerik = dosya.read()
print(icerik)
dosya.close()

print("\n3. SATIR SATIR OKUMA:")
dosya = open("hesap.txt", "r")
satırlar = dosya.readlines()
for satir in satırlar:
    print(f"- {satir.strip()}")
dosya.close()

print("\n4. DOSYA EKLEME (APPEND):")
dosya = open("hesap.txt", "a")
dosya.write("Faiz Orani: 0.05\n")
dosya.close()
print("Veri eklendi")

print("\n5. DOSYA OKUMA (Tekrar):")
dosya = open("hesap.txt", "r")
print(dosya.read())
dosya.close()

print("\n6. WITH STATEMENT (Otomatik Kapama):")
with open("hesap.txt", "r") as dosya:
    for satir in dosya:
        print(f"* {satir.strip()}")

print("\n7. DOSYA VAR MI KONTROL:")
if os.path.exists("hesap.txt"):
    print("hesap.txt var")
else:
    print("hesap.txt yok")

print("\n8. DOSYA BOYUTU:")
boyut = os.path.getsize("hesap.txt")
print(f"Boyut: {boyut} byte")

print("\n" + "=" * 50)
print("FINTECH UYGULAMALARI")
print("=" * 50)

print("\n1. MUSTERI VERISI YAZMA:")
with open("musteriler.txt", "w") as dosya:
    dosya.write("Musteri,Bakiye,Hesap_Tipi\n")
    dosya.write("Ahmet,5000,Vadesiz\n")
    dosya.write("Fatma,10000,Vadeli\n")
    dosya.write("Ali,7500,Tasarruf\n")
print("musteriler.txt olusturuldu")

print("\n2. MUSTERI VERISI OKUMA:")
with open("musteriler.txt", "r") as dosya:
    print(dosya.read())

print("\n3. CSV PARSE VE ISLEM:")
musteriler = []
with open("musteriler.txt", "r") as dosya:
    satırlar = dosya.readlines()[1:]
    for satir in satırlar:
        veri = satir.strip().split(",")
        musteriler.append({
            "ad": veri[0],
            "bakiye": int(veri[1]),
            "tip": veri[2]
        })

print("Musteriler:")
for m in musteriler:
    print(f"- {m['ad']}: {m['bakiye']} TL ({m['tip']})")

print("\n4. ISLEM KAYDI (LOG):")
with open("islemler.log", "w") as dosya:
    dosya.write("=== ISLEM KAYDI ===\n")
    dosya.write("Transfer: Ahmet -> Fatma: 1000 TL\n")
    dosya.write("Cekme: Ali: 500 TL\n")
    dosya.write("Yatirma: Fatma: 2000 TL\n")
print("islemler.log olusturuldu")

print("\n5. LOG OKUMA:")
with open("islemler.log", "r") as dosya:
    log = dosya.read()
    print(log)

print("\n6. BANKA HESAP YEDEGI:")
with open("hesap_yedek.txt", "w") as dosya:
    dosya.write("HESAP YEDEGI\n")
    dosya.write("=" * 30 + "\n")
    for m in musteriler:
        dosya.write(f"{m['ad']}: {m['bakiye']} TL\n")
print("hesap_yedek.txt olusturuldu")

print("\n7. YEDEK OKUMA:")
with open("hesap_yedek.txt", "r") as dosya:
    print(dosya.read())

print("\n8. DOSYA SILME:")
if os.path.exists("hesap.txt"):
    os.remove("hesap.txt")
    print("hesap.txt silindi")

print("\n9. DOSYA LISTESI:")
dosyalar = [f for f in os.listdir(".") if f.endswith(".txt") or 
f.endswith(".log")]
print(f"Dosyalar: {dosyalar}")

print("\n10. DOSYA RENAME:")
if os.path.exists("islemler.log"):
    os.rename("islemler.log", "transaction.log")
    print("islemler.log -> transaction.log")

print("\n" + "=" * 50)
print("OZET")
print("=" * 50)
print("- w: Yaz (Oversprite)")
print("- r: Oku")
print("- a: Ekle (Append)")
print("- with: Otomatik Kapama")
print("- os.path.exists(): Var mi Kontrol")
print("- os.remove(): Sil")
print("- os.listdir(): Dosya Listesi")
