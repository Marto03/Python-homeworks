list_1 = []
def input_nums(n):
    number = int(input("How much elements: "))
    for i in range(number):
        current_element = input(f"Input {i+1}: ")
        if current_element.isnumeric():

            list_1.append(int(current_element))

    return list_1
print(input_nums(1))