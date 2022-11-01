number = int(27102022)
print(number)

decimal = (input(f"Choose numerical system between binary(2) and hexadecimal(16): "))
if decimal == "binary":
    print(bin(number))
elif decimal == "2":
    print(bin(number))
elif decimal == "16":
    print(hex(number))
elif decimal == str("hexadecimal"):
    print(hex(number))
else:
    print("Invalid numerical system")



