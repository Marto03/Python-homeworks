#Second exercise , лице и периметър на окръжност
from math import pi

r = float(input())
perimeter = 2 * pi * r
S = pi * r**2
perimeter = str(round(perimeter, 3))
S = str(round(S, 3))
print(f'The S is :{S}')
print(f'The perimeter is:{perimeter}')
