# STRING METODLARI

print("=" * 50)
print("STRING METODLARI")
print("=" * 50)

print("\n1. UPPER / LOWER:")
metin = "Banka Hesabi"
print(f"Orijinal: {metin}")
print(f"Upper: {metin.upper()}")
print(f"Lower: {metin.lower()}")

print("\n2. STRIP:")
metin = "  Hesap  "
print(f"Strip: '{metin.strip()}'")
print(f"Lstrip: '{metin.lstrip()}'")
print(f"Rstrip: '{metin.rstrip()}'")

print("\n3. REPLACE:")
metin = "Bakiye 5000 TL"
print(f"Orijinal: {metin}")
print(f"Replace: {metin.replace('5000', '10000')}")

print("\n4. SPLIT / JOIN:")
metin = "Istanbul,Ankara,Izmir"
sehirler = metin.split(",")
print(f"Split: {sehirler}")
print(f"Join: {' - '.join(sehirler)}")

print("\n5. FIND / INDEX:")
metin = "Transfer basarili"
print(f"Find Transfer: {metin.find('Transfer')}")
print(f"Iceriyor: {'Transfer' in metin}")

print("\n6. ISDIGIT / ISALPHA:")
print(f"'12345' sayi: {'12345'.isdigit()}")
print(f"'Hesap' harf: {'Hesap'.isalpha()}")

print("\n" + "=" * 50)
print("FINTECH ORNEKLERI")
print("=" * 50)

print("\n1. IBAN KONTROL:")
def iban_gecerli(iban):
    iban = iban.strip().upper()
    if not iban.startswith("TR"):
        return False
    if len(iban) != 26:
        return False
    if not iban[2:].isdigit():
        return False
    return True

test = ["TR123456789012345678901234", "INVALID123"]
for i in test:
    print(f"{i}: {'OK' if iban_gecerli(i) else 'HATA'}")

print("\n2. EMAIL KONTROL:")
def email_gecerli(email):
    email = email.strip().lower()
    if "@" not in email:
        return False
    if "." not in email.split("@")[1]:
        return False
    return True

test = ["ahmet@bank.com", "invalid@com", "hata"]
for e in test:
    print(f"{e}: {'OK' if email_gecerli(e) else 'HATA'}")

print("\n3. TELEFON FORMAT:")
def telefon_format(num):
    num = num.strip()
    if num.startswith("+90"):
        num = num[3:]
    elif num.startswith("0"):
        num = num[1:]
    if len(num) != 10 or not num.isdigit():
        return "HATA"
    return f"+90 ({num[:3]}) {num[3:6]}-{num[6:]}"

test = ["05551234567", "+905551234567"]
for t in test:
    print(f"{t}: {telefon_format(t)}")

print("\n4. ISIM FORMAT:")
def isim_format(isim):
    return " ".join([w.capitalize() for w in isim.lower().split()])

test = ["AHMET YILMAZ", "fatma ozturk", "ali demir"]
for t in test:
    print(f"{t}: {isim_format(t)}")

print("\n5. SIFRE KONTROLU:")
def sifre_gucu(sifre):
    puan = 0
    if len(sifre) >= 8:
        puan += 1
    if any(c.isupper() for c in sifre):
        puan += 1
    if any(c.islower() for c in sifre):
        puan += 1
    if any(c.isdigit() for c in sifre):
        puan += 1
    if any(c in "!@#$%^&*" for c in sifre):
        puan += 1
    
    if puan == 0 or puan == 1:
        return "ZAYIF"
    elif puan == 2 or puan == 3:
        return "ORTA"
    else:
        return "KUVVETLI"

test = ["123456", "Pass123", "P@ssw0rd!"]
for t in test:
    print(f"{t}: {sifre_gucu(t)}")

print("\n6. CSV PARSE:")
def csv_parse(satir):
    return [d.strip() for d in satir.split(",")]

csv = "Ahmet, 5000, Vadesiz, Aktif"
veri = csv_parse(csv)
print(f"CSV: {csv}")
print(f"Musteri: {veri[0]}, Bakiye: {veri[1]} TL")
