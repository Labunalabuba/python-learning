# FONKSIYONLAR (FUNCTIONS)

print("=" * 50)
print("FONKSIYON TEMELLERI")
print("=" * 50)

def selamla():
    print("Hos geldiniz!")

selamla()

print("\n2. Parametreli Fonksiyon:")

def hesapla_faiz(tutar, oran):
    faiz = tutar * oran
    return faiz

faiz_tutari = hesapla_faiz(10000, 0.10)
print(f"10000 TL'nin yuzde 10'u: {faiz_tutari} TL")

print("\n3. Birden Fazla Parametre:")

def transfer_yap(gonderici, alici, tutar):
    print(f"{gonderici} -> {alici}: {tutar} TL")
    return "Transfer Basarili"

sonuc = transfer_yap("Ahmet", "Fatma", 500)
print(sonuc)

print("\n4. Default Deger:")

def kredi_hesapla(tutar, faiz_orani=0.10, vade=12):
    aylik_faiz = faiz_orani / 12
    aylik_odeme = tutar / vade * (1 + aylik_faiz)
    return aylik_odeme

print(f"Varsayilan: {kredi_hesapla(10000):.2f} TL")
print(f"Ozel: {kredi_hesapla(10000, 0.15, 24):.2f} TL")

print("\n5. Birden Fazla Return:")

def hesap_ozetleri(bakiye, tutar):
    yeni_bakiye = bakiye - tutar
    durum = "Basarili" if yeni_bakiye >= 0 else "Yetersiz Bakiye"
    return yeni_bakiye, durum

bakiye, durum = hesap_ozetleri(5000, 2000)
print(f"Yeni Bakiye: {bakiye} TL")
print(f"Durum: {durum}")

print("\n" + "=" * 50)
print("FINTECH FONKSIYONLARI")
print("=" * 50)

print("\n1. ATM Para Cekme:")

def atm_para_cek(bakiye, miktar):
    if miktar > 0 and miktar % 50 == 0:
        if bakiye >= miktar:
            yeni_bakiye = bakiye - miktar
            return yeni_bakiye, "Para cekildi"
        else:
            return bakiye, "Yetersiz bakiye"
    else:
        return bakiye, "Gecersiz miktar"

bakiye = 5000
bakiye, mesaj = atm_para_cek(bakiye, 250)
print(f"Bakiye: {bakiye} TL, {mesaj}")

print("\n2. Kredi Uygunlugu:")

def kredi_uygunlugu(yas, gelir, kredi_skoru, banka_sicili):
    if yas < 21:
        return False, "Yas sarti yetersiz"
    if gelir < 20000:
        return False, "Gelir yetersiz"
    if kredi_skoru < 650:
        return False, "Kredi skoru dusuk"
    if not banka_sicili:
        return False, "Banka siciliniz yok"
    return True, "Onaylandi"

uygun, mesaj = kredi_uygunlugu(35, 60000, 750, True)
print(mesaj)

print("\n3. Bilesik Faiz Hesabi:")

def bilesik_faiz(tutar, oran, yil):
    total = tutar * (1 + oran) ** yil
    kazanc = total - tutar
    return total, kazanc

total, kazanc = bilesik_faiz(10000, 0.10, 5)
print(f"Baslangic: 10000 TL")
print(f"5 Yil Sonra: {total:.2f} TL")
print(f"Kazanc: {kazanc:.2f} TL")

print("\n4. Odeme Plani:")

def odeme_plani(tutar, vade):
    aylik_tutar = tutar / vade
    plan = []
    for ay in range(1, vade + 1):
        plan.append({"ay": ay, "odeme": aylik_tutar, "kalan": tutar - 
(aylik_tutar * ay)})
    return plan

plan = odeme_plani(12000, 12)
print("Ilk 3 Ay:")
for odeme in plan[:3]:
    ay = odeme['ay']
    tutar = odeme['odeme']
    kalan = odeme['kalan']
    print(f"Ay {ay}: {tutar:.2f} TL (Kalan: {kalan:.2f} TL)")
