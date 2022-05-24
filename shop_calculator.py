total = 0
number_of_items = int(input("Enter the number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter the number of items: "))
for i in range(number_of_items):
    price = float(input("Enter the price of item: "))
    total += price
    print("Price of item: ",price)

    if total > 100:
        total = total*0.9
print("Total price for {} items is ${:.2f}".format(number_of_items, total))


