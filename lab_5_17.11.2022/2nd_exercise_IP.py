number = input("Write a number: ")
def pal(n):

    if number != n[::-1]:
        return 0
    else:
        return 1
print(pal(number))