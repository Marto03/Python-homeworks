from itertools import count

a = input("Write text: ")
dict = {}
for i in a:
    if i not in dict.keys():
        dict[i] = a.count(i)

print(dict, end=" ")

