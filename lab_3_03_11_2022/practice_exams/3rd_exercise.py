number = int(input("Write a number , factorial: "))
i = 1
sum = 0
for i in range(1, number+1):
    sum += i
    i += 1

print(f"Sum is: {sum}")
