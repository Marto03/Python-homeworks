list_1 = []
def list_avg(lst):
    n = int(input("How many elements: "))
    suma = 0
    for i in range(1, n + 1):
        number = input(f"Write element {i}: ")
        if number.isnumeric() or str(number).replace(".", "").isnumeric():
            list_1.append(number)
            suma += float(number)
            average = suma / len(list_1)

    return average

print(list_avg(1)) # Не знам дали трябва да го форматирам/закръглям затова го оставям така
print(list_1)
