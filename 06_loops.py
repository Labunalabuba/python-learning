# DÖNGÜLER (LOOPS)

print("=" * 50)
print("FOR DÖNGÜSÜ")
print("=" * 50)

# Basit for döngüsü
print("\n1. Basit sayı döngüsü:")
for i in range(1, 6):
    print(f"Sayı: {i}")

# Liste üzerinde döngü
print("\n2. Liste üzerinde döngü:")
bankalar = ["Ziraat", "İş Bankası", "Garanti", "Akbank"]
for banka in bankalar:
    print(f"Banka: {banka}")

# Döngüde index
print("\n3. Index ile döngü:")
for index, banka in enumerate(bankalar):
    print(f"{index + 1}. {banka}")

# Faiz hesabı döngüsü
print("\n4. Yıl yıl faiz hesabı:")
bakiye = 10000
faiz_orani = 0.10
for yil in range(1, 6):
    bakiye = bakiye * (1 + faiz_orani)
    print(f"Yıl {yil}: {bakiye:.2f} TL")

print("\n" + "=" * 50)
print("WHILE DÖNGÜSÜ")
print("=" * 50)

# While döngüsü
print("\n1. ATM para çekme:")
bakiye = 5000
cekilecek = 500

while bakiye >= cekilecek:
    bakiye -= cekilecek
    print(f"Para çekildi. Kalan bakiye: {bakiye} TL")

print(f"Yetersiz bakiye! Kalan: {bakiye} TL")

# While ile input
print("\n2. Kullanıcı girdisi ile:")
sifre = "1234"
giris_hakki = 3

while giris_hakki > 0:
    print(f"Giriş hakkınız: {giris_hakki}")
    giris_hakki -= 1
    if giris_hakki == 0:
        print("Giriş başarısız!")

print("\n" + "=" * 50)
print("BREAK VE CONTINUE")
print("=" * 50)

# Break
print("\n1. Break kullanımı:")
for i in range(1, 11):
    if i == 5:
        print("5'e ulaştık, çıkıyoruz!")
        break
    print(i)

# Continue
print("\n2. Continue kullanımı (çift sayıları atla):")
for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i)

print("\n" + "=" * 50)
print("NESTED LOOPS (İÇ İÇE DÖNGÜLER)")
print("=" * 50)

# Tablo oluştur
print("\n1. Çarpım tablosu:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="  ")
    print()

# Kredi ödeme planı
print("\n2. Kredi Ödeme Planı (3 ay, 2 taksit/ay):")
for ay in range(1, 4):
    print(f"\nAy {ay}:")
    taksit_tutari = 1000
    for taksit in range(1, 3):
        print(f"  Taksit {taksit}: {taksit_tutari} TL")
