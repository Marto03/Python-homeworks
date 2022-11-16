import random

n = random.randint(2, 20)


list_1 = random.sample(range(0, 50), n)
list_2 = []

for i in range(n):
    if (i % 2) == 0:
        list_2.append(list_1[i])
    else:
        list_2.append((list_1[i]+list_1[i-1]))
        list_2.append(list_1[i])

print(f"Size of list: {n}")
print(f"Random numbers list: {list_1}")
print(f"Last list: {list_2}")
