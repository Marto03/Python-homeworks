n = int(input("Input an int number: "))
list = []

for i in range(0, n):
    n2 = int(input("Input another int number: "))
    list.append(n2)

for i in range(0, n):
    n3 = int(input(f"Enter 0 or 1 for number '{i+1}': "))
    if n3 == 0:
        if i % 2 == 0:
            list[i] += 5
    elif n3 == 1:
        if i % 2 != 0:
            list[i] += 10
    else:
        print(f"Invalid number, write 0 or 1 for number '{i+1}': ")
print(list)
