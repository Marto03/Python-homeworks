number = int(input("How many rows: "))

for i in range(0, number+1):
    for j in range(number-i, 0, -1):
        print(j, end=' ')
    print()
