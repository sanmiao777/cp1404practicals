for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0,101,10):
    print(i, end=' ')
print()
for i in range(0,21):
    i =20-i
    print(i, end=' ')
print()
number = int(input("Number of stars: "))
for i in range(number):
    print('*', end='')
print()
row = 1
number = int(input("Number of stars: "))
while row <= number:
    col = 1
    while col <= row:
        print('*', end='')
        col +=1
    print('')
    row +=1
