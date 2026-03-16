print("=" * 50)
print("HATA YONETIMI TEMELLERI")
print("=" * 50)

print("\n1. TRY/EXCEPT:")
try:
    sayi = int("abc")
except ValueError:
    print("Hata: Sayi formati yanlis!")

print("\n2. BIRDEN FAZLA EXCEPT:")
try:
    dizi = [1, 2, 3]
    print(dizi[10])
except IndexError:
    print("Hata: Index yok!")

print("\n3. GENEL EXCEPTION:")
try:
    sonuc = 10 / 0
except Exception as e:
    print("Hata: " + str(e))

print("\n4. TRY/EXCEPT/ELSE:")
try:
    sayi = int("123")
except ValueError:
    print("Sayi formati yanlis!")
else:
    print("Basarili: " + str(sayi))

print("\n5. TRY/EXCEPT/FINALLY:")
try:
    dosya = open("test.txt", "r")
except FileNotFoundError:
    print("Hata: Dosya bulunamadi!")
finally:
    print("Finally blogu calistti")

print("\n6. CUSTOM EXCEPTION:")

class YetersizBakiye(Exception):
    pass

class Hesap:
    def __init__(self, bakiye):
        self.bakiye = bakiye
    
    def para_cek(self, miktar):
        if self.bakiye < miktar:
            raise YetersizBakiye("Yetersiz bakiye!")
        self.bakiye -= miktar
        print(str(miktar) + " TL cekildi")

try:
    h = Hesap(5000)
    h.para_cek(10000)
except YetersizBakiye as e:
    print("Hata: " + str(e))

print("\n7. TRANSFER:")

class TransferHatasi(Exception):
    pass

class HesapTransfer:
    def __init__(self, ad, bakiye):
        self.ad = ad
        self.bakiye = bakiye
    
    def transfer_yap(self, alici, miktar):
        if self.bakiye < miktar:
            raise TransferHatasi("Yetersiz bakiye!")
        self.bakiye -= miktar
        alici.bakiye += miktar
        print(str(miktar) + " TL transferi basarili")

h1 = HesapTransfer("Ahmet", 5000)
h2 = HesapTransfer("Fatma", 3000)

try:
    h1.transfer_yap(h2, 1000)
    print("Ahmet: " + str(h1.bakiye))
    print("Fatma: " + str(h2.bakiye))
except TransferHatasi as e:
    print("Hata: " + str(e))

print("\n8. EMAIL DOGRULAMA:")

class EmailHatasi(Exception):
    pass

def email_dogrula(email):
    if "@" not in email:
        raise EmailHatasi("Gecersiz email!")
    return True

emailler = ["ahmet@bank.com", "invalid", "fatma@gmail.com"]

for email in emailler:
    try:
        email_dogrula(email)
        print(email + ": OK")
    except EmailHatasi:
        print(email + ": HATA")

print("\n" + "=" * 50)
print("OZET")
print("=" * 50)
print("- try: Deneme")
print("- except: Hata yakala")
print("- raise: Hata olustur")
print("- finally: Her zaman")
