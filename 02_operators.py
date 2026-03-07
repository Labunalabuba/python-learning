# PYTHON OPERATÖRLERI

# ===== ARİTMETİK OPERATÖRLER =====
print("=== ARİTMETİK OPERATÖRLER ===")

toplam = 10 + 5
print(f"10 + 5 = {toplam}")

fark = 10 - 3
print(f"10 - 3 = {fark}")

carpim = 4 * 5
print(f"4 * 5 = {carpim}")

bolum = 15 / 3
print(f"15 / 3 = {bolum}")

tam_bolum = 15 // 3
print(f"15 // 3 = {tam_bolum}")

mod = 17 % 5
print(f"17 % 5 = {mod}")

ust = 2 ** 3
print(f"2 ** 3 = {ust}")

# ===== ATAMA OPERATÖRLERI =====
print("\n=== ATAMA OPERATÖRLERI ===")

para = 1000
print(f"Para: {para}")

para += 500
print(f"500 eklendi: {para}")

para -= 200
print(f"200 çıkarıldı: {para}")

para *= 2
print(f"2 ile çarpıldı: {para}")

# ===== KARŞILAŞTIRMA OPERATÖRLERI =====
print("\n=== KARŞILAŞTIRMA OPERATÖRLERI ===")

a = 10
b = 5

esit = (a == b)
print(f"{a} == {b}: {esit}")

esit_degil = (a != b)
print(f"{a} != {b}: {esit_degil}")

buyuk = (a > b)
print(f"{a} > {b}: {buyuk}")

kucuk = (a < b)
print(f"{a} < {b}: {kucuk}")

# ===== MANTIKSAL OPERATÖRLER =====
print("\n=== MANTIKSAL OPERATÖRLER ===")

kredi_onayli = True
gelir_yeterli = True
kredi_verilebilir = kredi_onayli and gelir_yeterli
print(f"Kredi verilebilir (AND): {kredi_verilebilir}")

param_var = False
kredi_alabilir = param_var or kredi_onayli
print(f"Kredi alabilir (OR): {kredi_alabilir}")

temiz_kredi = True
temerrut = not temiz_kredi
print(f"Temerrut var (NOT): {temerrut}")
