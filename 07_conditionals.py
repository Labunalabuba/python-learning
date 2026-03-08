# KOŞULLU İFADELER (IF, ELIF, ELSE)

print("=" * 50)
print("IF, ELIF, ELSE")
print("=" * 50)

# Basit if
print("\n1. Basit IF:")
yas = 25
if yas >= 18:
    print("Resit misiniz? EVET")

# if-else
print("\n2. IF-ELSE:")
bakiye = 500
cekilecek_miktar = 1000

if bakiye >= cekilecek_miktar:
    print("Para cekilebilir")
    bakiye -= cekilecek_miktar
else:
    print(f"Yetersiz bakiye! Bakiye: {bakiye} TL")

# if-elif-else
print("\n3. IF-ELIF-ELSE:")
kredi_skoru = 650

if kredi_skoru >= 750:
    faiz = 0.05
    print("Dusuk faiz: %5")
elif kredi_skoru >= 650:
    faiz = 0.10
    print("Orta faiz: %10")
else:
    faiz = 0.20
    print("Yuksek faiz: %20")

print(f"Sizin faiz orani: {faiz * 100}%")

# Nested if
print("\n4. Ic Ice IF (Kredi Uygunlugu):")
yas = 35
yillik_gelir = 60000
kredi_skoru = 700
istenen_kredi = 100000

if yas >= 21:
    print("Yas uygun")
    if yillik_gelir >= 30000:
        print("Gelir uygun")
        if kredi_skoru >= 650:
            print("Kredi skoru uygun")
            if istenen_kredi <= yillik_gelir * 3:
                print("KREDİ ONAYLANDI!")
            else:
                print("İstenen miktar cok yuksek")
        else:
            print("Kredi skoru yetersiz")
    else:
        print("Gelir yetersiz")
else:
    print("Yas sarti karsılamıyor")

print("\n" + "=" * 50)
print("MANTIKSAL OPERATÖRLER İLE")
print("=" * 50)

# AND
print("\n1. AND Operatörü:")
yas = 30
banka_sicili = True
istihdam_durumu = "Sabit"

if yas >= 25 and banka_sicili and istihdam_durumu == "Sabit":
    print("Kredi verilebilir")
else:
    print("Kredi verilemez")

# OR
print("\n2. OR Operatörü:")
email_dogrulama = True
telefon_dogrulama = False

if email_dogrulama or telefon_dogrulama:
    print("En az bir dogrulama basarili")
else:
    print("Dogrulama basarısız")

# NOT
print("\n3. NOT Operatörü:")
hesap_donmus = False

if not hesap_donmus:
    print("Hesap aktif, islem yapılabilir")
else:
    print("Hesap donmus, islem yapılamaz")

print("\n" + "=" * 50)
print("GERÇEK FINTECH ÖRNEKLERİ")
print("=" * 50)

# Banka işlemi
print("\n1. Para Transferi:")
gonderici_bakiye = 5000
alici_var = True
transfer_tutari = 2000

if gonderici_bakiye >= transfer_tutari and alici_var:
    gonderici_bakiye -= transfer_tutari
    print(f"Transfer basarili!")
    print(f"Yeni bakiye: {gonderici_bakiye} TL")
else:
    print("Transfer basarısız")

# Faiz hesabı
print("\n2. Faiz Hesabi:")
tutar = 50000
gun_sayisi = 365

if tutar >= 100000:
    faiz_orani = 0.04
    aciklama = "VIP musteri"
elif tutar >= 50000:
    faiz_orani = 0.03
    aciklama = "Normal musteri"
else:
    faiz_orani = 0.02
    aciklama = "Yeni musteri"

faiz = (tutar * faiz_orani * gun_sayisi) / 365
total = tutar + faiz

print(f"Tutar: {tutar} TL ({aciklama})")
print(f"Faiz Orani: {faiz_orani * 100}%")
print(f"Kazanilan Faiz: {faiz:.2f} TL")
print(f"Toplam: {total:.2f} TL")

# Hesap Türü Seçimi
print("\n3. Hesap Türü Secimi:")
aylık_gelir = 10000
calisma_durumu = "Emekli"
yas = 70

if yas < 25:
    hesap_turu = "Genc Hesabi"
    faydalar = ["Dusuk komisyon", "Bonus"]
elif yas >= 65:
    hesap_turu = "Emekli Hesabi"
    faydalar = ["Yuksek faiz", "Ucretsiz islemler"]
elif calisma_durumu == "Serbest Meslek":
    hesap_turu = "Esnaf Hesabi"
    faydalar = ["Vergi avantaji", "Isletme fonksiyonlari"]
else:
    hesap_turu = "Standart Hesap"
    faydalar = ["Normal faiz", "Standart hizmetler"]

print(f"Hesap Türü: {hesap_turu}")
print(f"Faydalar: {', '.join(faydalar)}")
