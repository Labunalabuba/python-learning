# OOP ILERI KONULAR - KALITIM, KAPSULLEME, POLIMORFIZM

print("=" * 50)
print("KALITIM (INHERITANCE)")
print("=" * 50)

print("\n1. ANA SINIF (PARENT CLASS):")

class Musteri:
    def __init__(self, ad, email):
        self.ad = ad
        self.email = email
    
    def bilgi(self):
        print(f"Ad: {self.ad}")
        print(f"Email: {self.email}")

m = Musteri("Ahmet", "ahmet@bank.com")
m.bilgi()

print("\n2. KALITIM YAPMA:")

class MusteriPremium(Musteri):
    def __init__(self, ad, email, uyelik_tarihi):
        super().__init__(ad, email)
        self.uyelik_tarihi = uyelik_tarihi
    
    def bilgi(self):
        super().bilgi()
        print(f"Uyelik: {self.uyelik_tarihi}")

mp = MusteriPremium("Fatma", "fatma@bank.com", "2024-01-01")
mp.bilgi()

print("\n3. BIRDEN FAZLA KALITIM:")

class HesapMusteri(Musteri):
    def __init__(self, ad, email, iban, bakiye):
        super().__init__(ad, email)
        self.iban = iban
        self.bakiye = bakiye
    
    def bilgi(self):
        super().bilgi()
        print(f"IBAN: {self.iban}")
        print(f"Bakiye: {self.bakiye} TL")

hm = HesapMusteri("Ali", "ali@bank.com", "TR001", 5000)
hm.bilgi()

print("\n" + "=" * 50)
print("KAPSULLEME (ENCAPSULATION)")
print("=" * 50)

print("\n1. PRIVATE ATTRIBUTE:")

class Hesap:
    def __init__(self, iban, ad, bakiye):
        self.iban = iban
        self.ad = ad
        self._bakiye = bakiye
    
    def bakiye_goster(self):
        return self._bakiye
    
    def para_yatir(self, miktar):
        if miktar > 0:
            self._bakiye += miktar
            print(f"{miktar} TL yatirildi")
        else:
            print("Tutar 0 dan buyuk olmali!")
    
    def para_cek(self, miktar):
        if miktar > 0 and self._bakiye >= miktar:
            self._bakiye -= miktar
            print(f"{miktar} TL cekti")
        else:
            print("Islem basarisiz!")

h = Hesap("TR001", "Ahmet", 5000)
print(f"Bakiye: {h.bakiye_goster()} TL")
h.para_yatir(1000)
print(f"Bakiye: {h.bakiye_goster()} TL")
h.para_cek(500)
print(f"Bakiye: {h.bakiye_goster()} TL")

print("\n2. PROPERTY KULLANMA:")

class HesapProperty:
    def __init__(self, iban, ad, bakiye):
        self.iban = iban
        self.ad = ad
        self._bakiye = bakiye
    
    @property
    def bakiye(self):
        return self._bakiye
    
    @bakiye.setter
    def bakiye(self, deger):
        if deger >= 0:
            self._bakiye = deger
        else:
            print("Bakiye negatif olamaz!")

hp = HesapProperty("TR002", "Fatma", 10000)
print(f"Bakiye: {hp.bakiye} TL")
hp.bakiye = 12000
print(f"Bakiye: {hp.bakiye} TL")
hp.bakiye = -1000

print("\n" + "=" * 50)
print("POLIMORFIZM (POLYMORPHISM)")
print("=" * 50)

print("\n1. AYNI METODU FARKLI SEKILDE KULLANMA:")

class KrediUrun:
    def __init__(self, musteri, miktar):
        self.musteri = musteri
        self.miktar = miktar
    
    def faiz_hesapla(self):
        pass
    
    def bilgi(self):
        print(f"Musteri: {self.musteri}")
        print(f"Miktar: {self.miktar} TL")
        print(f"Faiz: {self.faiz_hesapla()} TL")

class KrediKisisel(KrediUrun):
    def faiz_hesapla(self):
        return self.miktar * 0.15

class KrediTicari(KrediUrun):
    def faiz_hesapla(self):
        return self.miktar * 0.10

class KrediMortgage(KrediUrun):
    def faiz_hesapla(self):
        return self.miktar * 0.05

print("Kisisel Kredi:")
k1 = KrediKisisel("Ahmet", 10000)
k1.bilgi()

print("\nTicari Kredi:")
k2 = KrediTicari("ABC Sirket", 50000)
k2.bilgi()

print("\nMortgage:")
k3 = KrediMortgage("Ali", 200000)
k3.bilgi()

print("\n2. LOOP ILE POLIMORFIZM:")

krediler = [
    KrediKisisel("Ahmet", 10000),
    KrediTicari("ABC Sirket", 50000),
    KrediMortgage("Ali", 200000)
]

print("\nTum Krediler:")
for kredi in krediler:
    kredi.bilgi()
    print()

print("\n" + "=" * 50)
print("FINTECH ORNEKLERI")
print("=" * 50)

print("\n1. BANKA SINIFI HIYERARŞISI:")

class BankaUrun:
    def __init__(self, ad, ozellikler):
        self.ad = ad
        self.ozellikler = ozellikler
    
    def komisyon_hesapla(self):
        pass
    
    def aciklama(self):
        print(f"Urun: {self.ad}")
        print(f"Ozellikler: {self.ozellikler}")
        print(f"Komisyon: %{self.komisyon_hesapla()}")

class Transfer(BankaUrun):
    def komisyon_hesapla(self):
        return 0.5

class CekVasitasuyla(BankaUrun):
    def komisyon_hesapla(self):
        return 1.0

class DovizTransferi(BankaUrun):
    def komisyon_hesapla(self):
        return 2.5

print("Transfer:")
t = Transfer("Hızlı Transfer", "3 dakika icinde")
t.aciklama()

print("\nCek Vasitasuyla:")
c = CekVasitasuyla("Cek Isleme", "1 gun isleme")
c.aciklama()

print("\nDoviz Transferi:")
d = DovizTransferi("Uluslararasi Transfer", "2-3 gun")
d.aciklama()

print("\n2. MUSTERI YONETIMI:")

class MusteriTipi:
    def __init__(self, ad, email):
        self._ad = ad
        self._email = email
        self._islemler = []
    
    @property
    def ad(self):
        return self._ad
    
    @property
    def email(self):
        return self._email
    
    def islem_ekle(self, islem):
        self._islemler.append(islem)
    
    def islem_gecmisi(self):
        print(f"\n{self._ad} Islem Gecmisi:")
        for i in self._islemler:
            print(f"  - {i}")

class BieyselMusteri(MusteriTipi):
    def __init__(self, ad, email, tc):
        super().__init__(ad, email)
        self.tc = tc
    
    def bilgi(self):
        print(f"Tipi: Bireysel")
        print(f"Ad: {self._ad}")
        print(f"Email: {self._email}")
        print(f"TC: {self.tc}")

class KurumselMusteri(MusteriTipi):
    def __init__(self, ad, email, vergi_no):
        super().__init__(ad, email)
        self.vergi_no = vergi_no
    
    def bilgi(self):
        print(f"Tipi: Kurumsal")
        print(f"Ad: {self._ad}")
        print(f"Email: {self._email}")
        print(f"Vergi No: {self.vergi_no}")

bm = BieyselMusteri("Ahmet", "ahmet@bank.com", "12345678901")
bm.bilgi()
bm.islem_ekle("Transfer: 1000 TL")
bm.islem_ekle("Yatirma: 500 TL")
bm.islem_gecmisi()

print("\n" + "-" * 50 + "\n")

km = KurumselMusteri("ABC Sirket", "abc@company.com", "1234567890")
km.bilgi()
km.islem_ekle("Havale: 50000 TL")
km.islem_ekle("Bordro: 100000 TL")
km.islem_gecmisi()

print("\n" + "=" * 50)
print("OZET")
print("=" * 50)
print("- Kalitim: Siniftan yeni sinif olusturma")
print("- super(): Ust sinifa erişim")
print("- Private: _ ile başlayan attribute")
print("- Property: @property ile getter/setter")
print("- Polimorfizm: Ayni isimde farkli metod")
