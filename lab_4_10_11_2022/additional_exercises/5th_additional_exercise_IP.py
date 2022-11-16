
s1 = {6, 7, 8}
s2 = {1, 2, 3, 4}
final_set = []
for i in s1:
    if i in s2:
        final_set = s2 - s1
    elif s2.difference(s1):
        final_set = s1 | s2

print(final_set)
