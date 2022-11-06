number = 76542
reverse_number = 0
while number > 0:
    reminder = number % 10
    reverse_number = (reverse_number * 10) + reminder
    number //= 10
print(reverse_number)
