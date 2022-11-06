start = 25
end = 50
print(f"Prime numbers between {start} and {end} are: ")
for i in range(start, end+1):
    if i > 1:
        for k in range(2, i):
            if (i % k) == 0:
                break
        else:
            print(i)





