numbers = int(input("How many numbers: "))
i = 1
sum = 0
while i <= numbers:
    num = int(input(f"Enter number {i}: "))
    i += 1
    sum += num

print(sum)