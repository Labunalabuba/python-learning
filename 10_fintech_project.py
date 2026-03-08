# FINTECH PROJESI: BASIT BANKA SISTEMI

print("=" * 60)
print("BANKA YÖNETİM SİSTEMİ")
print("=" * 60)

musteriler = {}
islem_gecmisi = {}

def musteri_ac(musteri_id, ad, baslangic_bakiye=0):
    musteriler[musteri_id] = {
        "ad": ad,
        "bakiye": baslangic_bakiye,
        "kredi_skoru": 700
    }
    islem_gecmisi[musteri_id] = []
    print(f"Musteri acildi: {ad} (ID: {musteri_id})")

def para_yatir(musteri_id, tutar):
    if musteri_id not in musteriler:
        print("Musteri bulunamadi")
        return False
    
    if tutar <= 0:
        print("Gecersiz tutar")
        return False
    
    musteriler[musteri_id]["bakiye"] += tutar
    islem_gecmisi[musteri_id].append({
        "tip": "Yatirma",
        "tutar": tutar,
        "bakiye": musteriler[musteri_id]["bakiye"]
    })
    print(f"{tutar} TL yatirildi")
    return True

def para_cek(musteri_id, tutar):
    if musteri_id not in musteriler:
        print("Musteri bulunamadi")
        return False
    
    if tutar <= 0:
        print("Gecersiz tutar")
        return False
    
    if musteriler[musteri_id]["bakiye"] < tutar:
        bakiye = musteriler[musteri_id]["bakiye"]
        print(f"Yetersiz bakiye! Bakiye: {bakiye} TL")
        return False
    
    musteriler[musteri_id]["bakiye"] -= tutar
    islem_gecmisi[musteri_id].append({
        "tip": "Cekme",
        "tutar": -tutar,
        "bakiye": musteriler[musteri_id]["bakiye"]
    })
    print(f"{tutar} TL cekildi")
    return True

def transfer_yap(gonderici_id, alici_id, tutar):
    if gonderici_id not in musteriler or alici_id not in musteriler:
        print("Musteri bulunamadi")
        return False
    
    if tutar <= 0:
        print("Gecersiz tutar")
        return False
    
    if musteriler[gonderici_id]["bakiye"] < tutar:
        print("Yetersiz bakiye")
        return False
    
    musteriler[gonderici_id]["bakiye"] -= tutar
    islem_gecmisi[gonderici_id].append({
        "tip": "Transfer (Giden)",
        "tutar": -tutar,
        "alici": musteriler[alici_id]["ad"],
        "bakiye": musteriler[gonderici_id]["bakiye"]
    })
    
    musteriler[alici_id]["bakiye"] += tutar
    islem_gecmisi[alici_id].append({
        "tip": "Transfer (Gelen)",
        "tutar": tutar,
        "gonderici": musteriler[gonderici_id]["ad"],
        "bakiye": musteriler[alici_id]["bakiye"]
    })
    
    g_ad = musteriler[gonderici_id]["ad"]
    a_ad = musteriler[alici_id]["ad"]
    print(f"{g_ad} -> {a_ad}: {tutar} TL")
    return True

def bakiye_sorgula(musteri_id):
    if musteri_id not in musteriler:
        print("Musteri bulunamadi")
        return None
    
    musteri = musteriler[musteri_id]
    print(f"\n--- {musteri['ad']} ---")
    print(f"Bakiye: {musteri['bakiye']} TL")
    print(f"Kredi Skoru: {musteri['kredi_skoru']}/1000")
    return musteri["bakiye"]

def islem_gecmisi_goster(musteri_id):
    if musteri_id not in islem_gecmisi:
        print("Musteri bulunamadi")
        return
    
    musteri = musteriler[musteri_id]
    print(f"\n--- {musteri['ad']} Islem Gecmisi ---")
    
    if not islem_gecmisi[musteri_id]:
        print("Islem yok")
        return
    
    for i, islem in enumerate(islem_gecmisi[musteri_id], 1):
        bakiye = islem['bakiye']
        tutar = islem['tutar']
        print(f"{i}. {islem['tip']}: {tutar} TL (Bakiye: {bakiye} TL)")

def faiz_hesapla(musteri_id, yil=1):
    if musteri_id not in musteriler:
        print("Musteri bulunamadi")
        return
    
    bakiye = musteriler[musteri_id]["bakiye"]
    faiz_orani = 0.05
    faiz = bakiye * faiz_orani * yil
    total = bakiye + faiz
    
    print(f"\n--- Faiz Hesabi ---")
    print(f"Baslangic Bakiye: {bakiye} TL")
    print(f"Faiz Orani: %{faiz_orani * 100}")
    print(f"Sure: {yil} yil")
    print(f"Kazanilan Faiz: {faiz:.2f} TL")
    print(f"Toplam: {total:.2f} TL")

def kredi_uygun_mu(musteri_id, kredi_tutari):
    if musteri_id not in musteriler:
        print("Musteri bulunamadi")
        return False
    
    musteri = musteriler[musteri_id]
    
    print(f"\n--- Kredi Uygunlugu ---")
    print(f"Kredi Skoru: {musteri['kredi_skoru']}")
    print(f"Istenen Kredi: {kredi_tutari} TL")
    
    if musteri["kredi_skoru"] < 650:
        print("Kredi skoru yetersiz")
        return False
    
    if kredi_tutari > musteri["bakiye"] * 5:
        print("Istenen kredi cok yuksek")
        return False
    
    print("KREDİ UYGUN!")
    return True

# DEMO
print("\n1. MUSTERI ACMA")
print("-" * 60)
musteri_ac(1, "Ahmet Yilmaz", 5000)
musteri_ac(2, "Fatma Ozturk", 3000)
musteri_ac(3, "Ali Demir", 10000)

print("\n2. PARA ISLEMLERI")
print("-" * 60)
para_yatir(1, 2000)
para_cek(1, 1500)
bakiye_sorgula(1)

print("\n3. TRANSFER")
print("-" * 60)
transfer_yap(1, 2, 1000)
bakiye_sorgula(1)
bakiye_sorgula(2)

print("\n4. ISLEM GECMISI")
print("-" * 60)
islem_gecmisi_goster(1)

print("\n5. FAIZ HESABI")
print("-" * 60)
faiz_hesapla(1, 1)

print("\n6. KREDI UYGUNLUGU")
print("-" * 60)
kredi_uygun_mu(1, 50000)
kredi_uygun_mu(2, 100000)

print("\n7. TUM MUSTERILER")
print("-" * 60)
for musteri_id, musteri in musteriler.items():
    ad = musteri['ad']
    bakiye = musteri['bakiye']
    print(f"ID: {musteri_id}, Ad: {ad}, Bakiye: {bakiye} TL")
