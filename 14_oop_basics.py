# OOP - NESNE YONELIMLI PROGRAMLAMA (OBJECT ORIENTED PROGRAMMING)

print("=" * 50)
print("OOP TEMELLERI")
print("=" * 50)

print("\n1. SINIF TANIMLAMA:")

class Hesap:
    def __init__(self, ad, bakiye):
        self.ad = ad
        self.bakiye = bakiye
    
    def bilgi_goster(self):
        print(f"Hesap: {self.ad}")
        print(f"Bakiye: {self.bakiye} TL")

hesap1 = Hesap("Ahmet", 5000)
hesap1.bilgi_goster()

print("\n2. BIRDEN FAZLA NESNE:")

hesap2 = Hesap("Fatma", 10000)
hesap3 = Hesap("Ali", 7500)

print(f"Hesap 1: {hesap1.ad} - {hesap1.bakiye} TL")
print(f"Hesap 2: {hesap2.ad} - {hesap2.bakiye} TL")
print(f"Hesap 3: {hesap3.ad} - {hesap3.bakiye} TL")

print("\n3. METOD EKLEME:")

class Musteri:
    def __init__(self, ad, bakiye):
        self.ad = ad
        self.bakiye = bakiye
    
    def para_yatir(self, miktar):
        self.bakiye += miktar
        print(f"{self.ad} yatirdi: {miktar} TL")
    
    def para_cek(self, miktar):
        if self.bakiye >= miktar:
            self.bakiye -= miktar
            print(f"{self.ad} cekti: {miktar} TL")
        else:
            print("Yetersiz bakiye!")
    
    def bakiye_goster(self):
        print(f"Bakiye: {self.bakiye} TL")

m1 = Musteri("Ahmet", 5000)
m1.para_yatir(1000)
m1.para_cek(500)
m1.bakiye_goster()

print("\n4. INIT METODU:")

class Banka:
    def __init__(self, ad, lokasyon):
        self.ad = ad
        self.lokasyon = lokasyon
        self.musteriler = []
        print(f"{self.ad} bankas? olusturuldu")
    
    def musteri_ekle(self, musteri):
        self.musteriler.append(musteri)
        print(f"{musteri} eklendi")
    
    def musterileri_listele(self):
        print(f"{self.ad} bankas? musterileri:")
        for m in self.musteriler:
            print(f"  - {m}")

banka = Banka("Ziraat", "Istanbul")
banka.musteri_ekle("Ahmet")
banka.musteri_ekle("Fatma")
banka.musterileri_listele()

print("\n" + "=" * 50)
print("FINTECH ORNEKLERI")
print("=" * 50)

print("\n1. HESAP SINIFI:")

class HesapFintech:
    def __init__(self, iban, ad, bakiye):
        self.iban = iban
        self.ad = ad
        self.bakiye = bakiye
        self.islemler = []
    
    def transfer_gonder(self, alici, miktar):
        if self.bakiye >= miktar:
            self.bakiye -= miktar
            self.islemler.append(f"Transfer: {alici} - {miktar} TL")
            print(f"{alici} ye {miktar} TL gonderildi")
        else:
            print("Yetersiz bakiye!")
    
    def para_yatir(self, miktar):
        self.bakiye += miktar
        self.islemler.append(f"Yatirma: {miktar} TL")
        print(f"{miktar} TL yatirildi")
    
    def islem_gecmisi(self):
        print(f"\n{self.ad} Islem Gecmisi:")
        for islem in self.islemler:
            print(f"  - {islem}")
    
    def bilgi(self):
        print(f"\nHesap Bilgileri:")
        print(f"  IBAN: {self.iban}")
        print(f"  Ad: {self.ad}")
        print(f"  Bakiye: {self.bakiye} TL")

h1 = HesapFintech("TR123", "Ahmet", 5000)
h1.transfer_gonder("Fatma", 1000)
h1.para_yatir(500)
h1.islem_gecmisi()
h1.bilgi()

print("\n2. BANKA SINIFI:")

class BankaFintech:
    def __init__(self, ad):
        self.ad = ad
        self.hesaplar = {}
    
    def hesap_ac(self, iban, musteri_ad, baslangic_bakiye):
        self.hesaplar[iban] = HesapFintech(iban, musteri_ad, 
baslangic_bakiye)
        print(f"{musteri_ad} icin hesap acildi")
    
    def hesap_getir(self, iban):
        return self.hesaplar.get(iban)
    
    def toplam_bakiye(self):
        toplam = sum([h.bakiye for h in self.hesaplar.values()])
        return toplam
    
    def bilgi(self):
        print(f"\n{self.ad} Bilgileri:")
        print(f"  Toplam Hesap: {len(self.hesaplar)}")
        print(f"  Toplam Bakiye: {self.toplam_bakiye()} TL")

banka = BankaFintech("Ziraat Bank")
banka.hesap_ac("TR001", "Ahmet", 5000)
banka.hesap_ac("TR002", "Fatma", 10000)
banka.hesap_ac("TR003", "Ali", 7500)

hesap_ahmet = banka.hesap_getir("TR001")
hesap_ahmet.transfer_gonder("Fatma", 1000)

banka.bilgi()

print("\n3. KREDI SINIFI:")

class Kredi:
    def __init__(self, musteri, miktar, oran):
        self.musteri = musteri
        self.miktar = miktar
        self.oran = oran
        self.odenmiş = 0
    
    def ode(self, tutar):
        faiz = self.miktar * self.oran
        toplam = self.miktar + faiz
        
        if self.odenmiş + tutar <= toplam:
            self.odenmiş += tutar
            print(f"{self.musteri} kredi odedi: {tutar} TL")
        else:
            print("Cok fazla tutar!")
    
    def durum(self):
        faiz = self.miktar * self.oran
        toplam = self.miktar + faiz
        kalan = toplam - self.odenmiş
        
        print(f"\n{self.musteri} Kredi Durumu:")
        print(f"  Anaparas: {self.miktar} TL")
        print(f"  Faiz: {faiz} TL")
        print(f"  Toplam: {toplam} TL")
        print(f"  Odenen: {self.odenmiş} TL")
        print(f"  Kalan: {kalan} TL")

kredi = Kredi("Ahmet", 10000, 0.1)
kredi.ode(2000)
kredi.ode(2000)
kredi.durum()

print("\n" + "=" * 50)
print("OZET")
print("=" * 50)
print("- class: Sinif tanimlama")
print("- __init__: Constructor metod")
print("- self: Nesnenin kendisine referans")
print("- metod: Sinifdeki fonksiyon")
print("- nesne: Siniftan olusturulan ornek")
