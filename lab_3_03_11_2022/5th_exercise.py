a = list(input("a="))
position = input("position=")
b = ""
for i in position:
    b += a[int(i)-1]
print(f"Number: {b}")
print(f"Sum: {sum([int(i) for i in a])}")
