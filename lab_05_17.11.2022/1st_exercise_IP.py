a = 0
b = 0
def triangle(a, b):
    if figure == "triangle":
        a = int(input("Input a: "))
        b = int(input("Input b: "))
    s = (a * b) / 2
    return s
def rectangle(a, b):
    if figure == "rectangle":
        a = int(input("Input a: "))
        b = int(input("Input b: "))
    s = a * b
    return s
def square(a):
    if figure == "square":
        a = int(input("Input a: "))
    s = a ** 2
    return s
figure = input("Write a geometric figure: ")
if figure == "square":
    print(square(a))
elif figure == "triangle":
    print(triangle(a, b))
elif figure == "rectangle":
    print(rectangle(a, b))
else:
    print("Invalid figure")
    print("Please write another figure")

