n = int(input("Input an int number: "))
dict = {}

for i in range(0, n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict[key] = value
m = int(input("Input another int number: "))
list = []
for i in range(0, m):
    value = input("Enter value: ")
    list.append(value)

print(dict)
print(list)

for i in range(0, m):
    for key in dict:
        if list[i] == key:
            list[i] = dict[key]

print(list)