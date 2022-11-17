def add(a, b):
    return a + b
def subst(a, b):
    return  a - b
def multiplication(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cant divide by 0"
    else:
        return a / b

print("Choose operation from 1 to 4: ")
choice = input("1. add\n2. substract\n3. multiply\n4. divide\nEnter the number of the operation ---> ")
a = int(input("Enter number 1 --> "))
b = int(input("Enter number 2 --> "))
if choice == "1":
    print(add(a, b))
elif choice == "2":
    print(subst(a, b))
elif choice == "3":
    print(multiplication(a, b))
elif choice == "4":
    print(divide(a, b))
else:
    print("invalid input")

