a = 0
b = 0
def max_of_two(n1, n2):
    n1 = input("Input number 1: ")
    n2 = input("Input number 2: ")
    if n1.replace(".", "").isnumeric() and n2.replace(".", "").isnumeric():
        if float(n1) >= float(n2):
            return n1
        else:
            return n2
    elif n1.replace(".", "").isnumeric():
        return n1
    elif n2.replace(".", "").isnumeric():
        return n2
    else:
        return

print(max_of_two(a, b))