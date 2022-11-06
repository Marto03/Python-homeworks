number = 5
for i in range(0, number):
    for j in range(0, i + 1):
        print("*", end=" ")
    print(" ")

for k in range(1, number):
    for l in range(number - k, 0, -1):
        print("*", end=" ")
    print(" ")