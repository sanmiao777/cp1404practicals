number = int(input("Number of items: "))
total = 0
while number < 1:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for number in range(1, number + 1):
    price = float(input("Price of item : "))
    total += price
if total > 100:
     total = total * 0.9
     print("Total price for",number,"items is",total)
else:
    print("Total price for", number, "items is", total)
