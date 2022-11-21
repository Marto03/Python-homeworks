def is_valid_triangle(a, b, c):
    if number_1 + number_2 >= number_3 and number_2 + number_3 >= number_1 and number_1 + number_3 >= number_2:
        return True
    else:
        return False

#def can_triangle_exist(a, b, c):
#    return is_valid_triangle(number_1, number_2, number_3)

number_1 = int(input("Input A: "))
number_2 = int(input("Input B: "))
number_3 = int(input("Input C: "))
can_triangle_exist = is_valid_triangle(number_1, number_2, number_3)
print(can_triangle_exist)