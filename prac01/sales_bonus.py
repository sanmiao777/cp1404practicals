sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * 0.1
elif sales >= 1000:
    bonus = sales * 0.15
print(bonus)