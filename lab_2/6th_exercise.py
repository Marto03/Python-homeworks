num = list(input("Enter num: "))
position = input("Enter position: ")
new_num = ""
for i in position:
    new_num += num[int(i)-1]
print(f"New num: {new_num}")
print(f"Sum: {sum([int(i) for i in num])}")

