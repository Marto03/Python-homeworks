number = int(input("Enter a number: "))
line = "*"
for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(line, end=" ")
    i += 1
    print("")