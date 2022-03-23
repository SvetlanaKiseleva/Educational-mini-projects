money = float(input("Введите сумму депозита:"))

per_cent = {"TKB": 5.6, "SKB": 5.9, "VTB": 4.28, "SBER": 4.0}
TKB = float(round(money/100*per_cent["TKB"], 2))
SKB = float(round(money/100*per_cent["SKB"], 2))
VTB = float(round(money/100*per_cent["VTB"], 2))
SBER = float(round(money/100*per_cent["SBER"], 2))
deposit = [TKB, SKB, VTB, SBER]
print(deposit)

d = {"TKB": TKB, "SKB": SKB, "VTB": VTB, "SBER": SBER}
i = max(d.values())
print(i)