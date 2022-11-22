list_1 = []
def input_nums(n):
#    number = int(input("How much elements: "))
    for i in range(n):
        current_element = input(f"Input {i+1}: ")
        if current_element.isnumeric():

            list_1.append(int(current_element))

    return list_1

def sum_list(lst):
    i = 0
    for n in lst:
        if str(n).isnumeric():

            i += int(n)
        elif str(n).replace(".", "").isnumeric():
            i += float(n)
    return i

a = 0
b = 0
def max_of_two(n1, n2):
#    n1 = input("Input number 1: ")
#    n2 = input("Input number 2: ")
    if str(n1).replace(".", "").isnumeric() and str(n2).replace(".", "").isnumeric():
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

print(max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2"))