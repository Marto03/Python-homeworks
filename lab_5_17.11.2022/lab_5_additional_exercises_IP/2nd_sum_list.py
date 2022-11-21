list_1 = []

def sum_list(lst):
    i = 0
    for n in lst:
        if str(n).isnumeric():

            i += int(n)
        elif str(n).replace(".", "").isnumeric():
            i += float(n)
    return i

print(sum_list([1, 3.3, '5', "a"]))