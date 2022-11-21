
def digitize(num):
    return tuple(map(int, str(num)))

print(digitize(123))
print(type(digitize(123)))