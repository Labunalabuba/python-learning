print("=" * 50)
print("VERITABANI (DATABASE - SQLite)")
print("=" * 50)

import sqlite3

print("\n1. VERITABANI OLUSTUR:")

baglanti = sqlite3.connect("bank.db")
imlek = baglanti.cursor()

imlek.execute("""
    CREATE TABLE IF NOT EXISTS musteriler (
        id INTEGER PRIMARY KEY,
        ad TEXT NOT NULL,
        email TEXT UNIQUE,
        bakiye REAL DEFAULT 0
    )
""")

baglanti.commit()
print("Musteriler tablosu olusturuldu")

print("\n2. VERI EKLE (INSERT):")

imlek.execute("INSERT INTO musteriler (ad, email, bakiye) VALUES (?, ?, ?)", 
              ("Ahmet Yilmaz", "ahmet@bank.com", 5000))
imlek.execute("INSERT INTO musteriler (ad, email, bakiye) VALUES (?, ?, ?)", 
              ("Fatma Kaya", "fatma@bank.com", 10000))
imlek.execute("INSERT INTO musteriler (ad, email, bakiye) VALUES (?, ?, ?)", 
              ("Ali Demir", "ali@bank.com", 7500))

baglanti.commit()
print("3 musteri eklendi")

print("\n3. VERI OKU (SELECT):")

imlek.execute("SELECT * FROM musteriler")
sonuc = imlek.fetchall()

print("Tum Musteriler:")
for satir in sonuc:
    print("ID: " + str(satir[0]) + ", Ad: " + satir[1] + ", Email: " + satir[2] + ", Bakiye: " + str(satir[3]))

print("\n4. KOSUL ILE OKU (WHERE):")

imlek.execute("SELECT * FROM musteriler WHERE bakiye > ?", (7000,))
sonuc = imlek.fetchall()

print("7000 TL dan fazla bakiyesi olanlar:")
for satir in sonuc:
    print("- " + satir[1] + " (" + str(satir[3]) + ")")

print("\n5. VERI GUNCELLE (UPDATE):")

imlek.execute("UPDATE musteriler SET bakiye = ? WHERE ad = ?", (6000, "Ahmet Yilmaz"))
baglanti.commit()

print("Ahmet Yilmaz bakiyesi 6000 olarak guncellendi")

print("\n6. VERI SIL (DELETE):")

imlek.execute("DELETE FROM musteriler WHERE ad = ?", ("Ali Demir",))
baglanti.commit()

print("Ali Demir silindi")

print("\n7. SAYMA (COUNT):")

imlek.execute("SELECT COUNT(*) FROM musteriler")
sonuc = imlek.fetchone()

print("Toplam Musteri Sayisi: " + str(sonuc[0]))

print("\n8. TOPLAM HESAPLA (SUM):")

imlek.execute("SELECT SUM(bakiye) FROM musteriler")
sonuc = imlek.fetchone()

print("Toplam Bakiye: " + str(sonuc[0]))

print("\n" + "=" * 50)
print("ISLEM GECMISI TABLOSU")
print("=" * 50)

print("\n1. ISLEM TABLOSU OLUSTUR:")

imlek.execute("""
    CREATE TABLE IF NOT EXISTS islemler (
        id INTEGER PRIMARY KEY,
        gonderici_id INTEGER,
        alici_id INTEGER,
        miktar REAL,
        tarih TEXT,
        FOREIGN KEY (gonderici_id) REFERENCES musteriler(id),
        FOREIGN KEY (alici_id) REFERENCES musteriler(id)
    )
""")

baglanti.commit()
print("Islemler tablosu olusturuldu")

print("\n2. ISLEM KAYIT:")

imlek.execute("INSERT INTO islemler (gonderici_id, alici_id, miktar, tarih) VALUES (?, ?, ?, ?)",
              (1, 2, 500, "2024-03-01"))
imlek.execute("INSERT INTO islemler (gonderici_id, alici_id, miktar, tarih) VALUES (?, ?, ?, ?)",
              (2, 1, 1000, "2024-03-02"))

baglanti.commit()
print("Islemler kaydedildi")

print("\n3. ISLEM GECMISI OKU:")

imlek.execute("""
    SELECT m1.ad, m2.ad, i.miktar, i.tarih 
    FROM islemler i
    JOIN musteriler m1 ON i.gonderici_id = m1.id
    JOIN musteriler m2 ON i.alici_id = m2.id
""")

sonuc = imlek.fetchall()

print("Islem Gecmisi:")
for satir in sonuc:
    print(satir[0] + " -> " + satir[1] + ": " + str(satir[2]) + " TL (" + satir[3] + ")")

print("\n" + "=" * 50)
print("FINTECH UYGULAMASI")
print("=" * 50)

print("\n1. BANKA SINIFI:")

class BankaHeAstap:
    def __init__(self, db_adi="bank.db"):
        self.baglanti = sqlite3.connect(db_adi)
        self.imlek = self.baglanti.cursor()
    
    def musteri_ekle(self, ad, email, bakiye=0):
        self.imlek.execute("INSERT INTO musteriler (ad, email, bakiye) VALUES (?, ?, ?)",
                          (ad, email, bakiye))
        self.baglanti.commit()
        print("Musteri eklendi: " + ad)
    
    def transfer(self, gonderici_ad, alici_ad, miktar):
        self.imlek.execute("SELECT id FROM musteriler WHERE ad = ?", (gonderici_ad,))
        gonderici = self.imlek.fetchone()
        
        self.imlek.execute("SELECT id FROM musteriler WHERE ad = ?", (alici_ad,))
        alici = self.imlek.fetchone()
        
        if gonderici is None or alici is None:
            print("Hata: Musteri bulunamadi")
            return
        
        self.imlek.execute("SELECT bakiye FROM musteriler WHERE id = ?", (gonderici[0],))
        bakiye = self.imlek.fetchone()[0]
        
        if bakiye < miktar:
            print("Hata: Yetersiz bakiye")
            return
        
        yeni_bakiye_1 = bakiye - miktar
        self.imlek.execute("UPDATE musteriler SET bakiye = ? WHERE id = ?", 
                          (yeni_bakiye_1, gonderici[0]))
        
        self.imlek.execute("SELECT bakiye FROM musteriler WHERE id = ?", (alici[0],))
        bakiye_2 = self.imlek.fetchone()[0]
        yeni_bakiye_2 = bakiye_2 + miktar
        self.imlek.execute("UPDATE musteriler SET bakiye = ? WHERE id = ?", 
                          (yeni_bakiye_2, alici[0]))
        
        self.imlek.execute("INSERT INTO islemler (gonderici_id, alici_id, miktar, tarih) VALUES (?, ?, ?, ?)",
                          (gonderici[0], alici[0], miktar, "2024-03-16"))
        
        self.baglanti.commit()
        print(str(miktar) + " TL transfer basarili")
    
    def bakiye_sor(self, ad):
        self.imlek.execute("SELECT bakiye FROM musteriler WHERE ad = ?", (ad,))
        sonuc = self.imlek.fetchone()
        if sonuc:
            print(ad + " bakiyesi: " + str(sonuc[0]))
        else:
            print("Musteri bulunamadi")
    
    def kapat(self):
        self.baglanti.close()

banka = BankaHeAstap()

print("\n2. TRANSFER ISLEM:")

banka.transfer("Ahmet Yilmaz", "Fatma Kaya", 1000)

print("\n3. BAKIYE SORGULA:")

banka.bakiye_sor("Ahmet Yilmaz")
banka.bakiye_sor("Fatma Kaya")

print("\n4. TUM MUSTERILER:")

imlek.execute("SELECT ad, bakiye FROM musteriler")
sonuc = imlek.fetchall()

print("Musteri Listesi:")
for satir in sonuc:
    print("- " + satir[0] + ": " + str(satir[1]) + " TL")

banka.kapat()

print("\n" + "=" * 50)
print("OZET")
print("=" * 50)
print("- sqlite3.connect(): Veritabani baglantisi")
print("- execute(): SQL komutu calistir")
print("- commit(): Degisiklikleri kaydet")
print("- fetchone(): Bir satir oku")
print("- fetchall(): Tum satirlari oku")
print("- CREATE TABLE: Tablo olustur")
print("- INSERT: Veri ekle")
print("- SELECT: Veri oku")
print("- UPDATE: Veri guncelle")
print("- DELETE: Veri sil")
