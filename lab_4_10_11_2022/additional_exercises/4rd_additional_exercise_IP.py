n = int(input("Input number: "))
new_num = n

i = 0
new_num_1 = 0
suma = 0
while i <= n:
    new_num_1 = new_num_1 * 10 + n
    i += 1
    suma += new_num_1

    if i != n:
        print(new_num_1, end="+")

    elif i == n:
        print(new_num_1, end="=")
        i += 1

print(suma)