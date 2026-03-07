# PRATIK ALIŞTIRMALAR

print("=" * 50)
print("PYTHON TEMEL KAVRAMLARI - ALIŞTIRMALAR")
print("=" * 50)

# ALIŞTIRMA 1: Yatırım Portföyü Hesapla
print("\n1️⃣  ALIŞTIRMA 1: Yatırım Portföyü")
print("-" * 50)

hisse_yatirim = 50000  # TL
hisse_kazanc_yuzde = 0.15  # %15

tahvil_yatirim = 30000  # TL
tahvil_kazanc_yuzde = 0.08  # %8

hisse_kazanc = hisse_yatirim * hisse_kazanc_yuzde
tahvil_kazanc = tahvil_yatirim * tahvil_kazanc_yuzde

toplam_yatirim = hisse_yatirim + tahvil_yatirim
toplam_kazanc = hisse_kazanc + tahvil_kazanc

print(f"Hisse Yatırımı: {hisse_yatirim} TL")
print(f"Hisse Kazancı (%15): {hisse_kazanc:.2f} TL")
print(f"\nTahvil Yatırımı: {tahvil_yatirim} TL")
print(f"Tahvil Kazancı (%8): {tahvil_kazanc:.2f} TL")
print(f"\nToplam Yatırım: {toplam_yatirim} TL")
print(f"Toplam Kazanç: {toplam_kazanc:.2f} TL")
print(f"Yüzdesel Hisse Dağılımı: {(hisse_yatirim / toplam_yatirim * 100):.1f}%")

# ALIŞTIRMA 2: IBAN Gizle
print("\n\n2️⃣  ALIŞTIRMA 2: IBAN Gizleme")
print("-" * 50)

iban = "TR12345678901234567890"
iban_gizli = iban[:4] + "*" * (len(iban) - 8) + iban[-4:]

print(f"Orijinal IBAN: {iban}")
print(f"Gizli IBAN:    {iban_gizli}")

# ALIŞTIRMA 3: Kredi Uygunluk Kontrolü
print("\n\n3️⃣  ALIŞTIRMA 3: Kredi Uygunluk Kontrolü")
print("-" * 50)

aylık_gelir = 5000  # TL
istenen_kredi = 50000  # TL
mevcut_borclar = 10000  # TL
kredi_skoru = 750  # 0-1000

# Kredi şartları
gelir_yeterli = istenen_kredi <= aylık_gelir * 12
borc_orani_ok = mevcut_borclar / aylık_gelir < 0.5
kredi_skoru_ok = kredi_skoru >= 700

kredi_onay = gelir_yeterli and borc_orani_ok and kredi_skoru_ok

print(f"Aylık Gelir: {aylık_gelir} TL")
print(f"İstenen Kredi: {istenen_kredi} TL")
print(f"Mevcut Borçlar: {mevcut_borclar} TL")
print(f"Kredi Skoru: {kredi_skoru}/1000")

print(f"\nKontroller:")
print(f"✓ Gelir Yeterli: {gelir_yeterli}")
print(f"✓ Borç Oranı OK: {borc_orani_ok}")
print(f"✓ Kredi Skoru OK: {kredi_skoru_ok}")

print(f"\n🎯 KREDİ ONAY: {'✅ ONAYLANDI' if kredi_onay else '❌ REDDEDİLDİ'}")
