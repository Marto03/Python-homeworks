from mymodule_1st_exercise import *
text = input("Area of which figure: ")
try:

    if text == "rhomb" or text == "triangle":
        a = float(input("A = "))
        h = float(input("H = "))
        if a == 0 or h == 0:
            raise NumberZero
        elif a < 0 or h < 0:
            raise NegativeNumber

        print(f"Area of {text} is : {rhomb(a, h)}")

    elif text == "rectangle":
        a = float(input("A = "))
        b = float(input("B = "))
        if a == 0 or b == 0:
            raise NumberZero
        elif a < 0 or b < 0:
            raise NegativeNumber

        print(f"Area of {text} is : {rectangle(a, b)}")

    elif text == "square":
        a = float(input("A = "))
        print(f"Area of {text} is : {square(a)}")
        if a == 0:
            raise NumberZero
        elif a < 0:
            raise NegativeNumber

    elif text == "traphezoid":
        a = float(input("A = "))
        b = float(input("B = "))
        h = float(input("H = "))
        if a == 0 or b == 0 or h == 0:
            raise NumberZero
        elif a < 0 or b < 0 or h < 0:
            raise NegativeNumber
        print(f"Area of {text} is : {traphezoid(a, b, h)}")



except NumberZero:
    print("Cant have 0 as length!")
except NegativeNumber:
    print("Negative length in figures doesn't exist!")

