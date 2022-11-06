rows = int(input("How many rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")

    i += 1
    print("")