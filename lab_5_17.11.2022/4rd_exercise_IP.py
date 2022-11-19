def list_1():
    list_2 = []
    number_1 = int(input("How many numbers: "))
    n = int(input("Input a number: "))
    for i in range(1, number_1 + 1):
        number_2 = int(input(f"Number {i}: "))

        if number_2 > n:
            number_2 = 0
        list_2.append(number_2)
    return list_2

print(list_1())