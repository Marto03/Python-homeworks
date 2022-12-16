from mymodule_2nd_exercise import *
try:
    a = int(input("Input A: "))
    b = int(input("Input B: "))

    operation = input("What operation to be done: ")
    if b == 0 and operation == "/" or operation == "division":
        raise ZeroDivisionError
    if operation == "add" or operation == "+":
        print(add(a, b))
    elif operation == "minus" or operation == "-":
        print(substract(a, b))
    elif operation == "multiplication" or operation == "*":
        print(multiplication(a, b))
    elif operation == "division" or operation == "/":
        print(division(a, b))
    else:
        raise WrongOperation

except ValueError:
    print("Invalid number")
except WrongOperation:
    print("Wrong operation")
except ZeroDivisionError:
    print("Cant divide by 0")