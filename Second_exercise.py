#Second exercise , лице и периметър на окръжност
from math import pi

r = float(input("r = "))
perimeter = 2 * pi * r
S = pi * r**2
perimeter = float(round(perimeter, 3))
S = float(round(S, 3))
print(f'The S is :{S}')
print(f'The perimeter is:{perimeter}')
