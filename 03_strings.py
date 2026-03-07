# STRING (METİN) İŞLEMLERİ

metin = "Python Fintech"

# ===== TEMEL STRING METODLARı =====
print("=== STRING METODLARI ===")

print(f"Orijinal: {metin}")
print(f"Büyük harf: {metin.upper()}")
print(f"Küçük harf: {metin.lower()}")
print(f"Uzunluk: {len(metin)}")
print(f"'o' sayısı: {metin.count('o')}")

# ===== STRING BÖLME VE BİRLEŞTİRME =====
print("\n=== BÖLME VE BİRLEŞTİRME ===")

cumle = "Hukuk, Finans, Teknoloji"
kelimeler = cumle.split(", ")
print(f"Kelimeler: {kelimeler}")

birlestirilmis = " - ".join(kelimeler)
print(f"Birleştirilmiş: {birlestirilmis}")

# ===== ARAMA VE DEĞİŞTİRME =====
print("\n=== ARAMA VE DEĞİŞTİRME ===")

hesap = "IBAN: TR12 3456 7890 1234 5678"
hesap_gizli = hesap.replace("3456", "****")
print(f"Orijinal: {hesap}")
print(f"Gizli: {hesap_gizli}")

# ===== STRING FORMATLAMA =====
print("\n=== STRING FORMATLAMA ===")

ad = "Labunalabuba"
tutar = 5000
faiz = 12.5

print(f"Hesap sahibi: {ad}, Tutar: {tutar} TL, Faiz: {faiz}%")
