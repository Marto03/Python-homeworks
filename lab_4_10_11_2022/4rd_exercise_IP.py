n = int(input("Input a number: "))

list_1 = []
dict = {}

for i in range(1, n + 1):

    list_1.append(i)

for i in range(0, len(list_1)):
    dict[list_1[i]] = list_1[len(list_1)-1-i]

print(f"{list_1} \n{dict}")
