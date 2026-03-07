# KREDI HESAPLAYICI - Fintech Örneği

print("=" * 40)
print("KREDİ HESAPLAYICI")
print("=" * 40)

# Girdiler
anapara = 100000  # TL
yillik_faiz = 0.12  # %12
vade = 12  # ay

print(f"\nKredi Bilgileri:")
print(f"Ana Para: {anapara} TL")
print(f"Yıllık Faiz: {yillik_faiz * 100}%")
print(f"Vade: {vade} ay")

# Hesaplamalar
aylik_faiz = yillik_faiz / 12
toplam_faiz = anapara * yillik_faiz * (vade / 12)
aylik_odeme = (anapara + toplam_faiz) / vade

print(f"\nHesaplanan Değerler:")
print(f"Aylık Faiz Oranı: {aylik_faiz * 100:.2f}%")
print(f"Toplam Faiz: {toplam_faiz:.2f} TL")
print(f"Aylık Ödeme: {aylik_odeme:.2f} TL")
print(f"Toplam Ödeme: {anapara + toplam_faiz:.2f} TL")
