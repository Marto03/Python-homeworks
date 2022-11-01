number = int(input("Write an integer number: "))
bit = int(input("Write a bit from this number: "))
if number & (1 << bit) > 0:
    print(False)
elif number & (1 << bit) == 0:
    print(True)
print(bin(number))