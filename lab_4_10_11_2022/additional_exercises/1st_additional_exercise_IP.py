n = int(input("Input a number you want to get Fibonacci: "))

n1, n2 = 0, 1
counter = 0

if n <= 0:
    print("Invalid")
else:
    while counter < n + 2:
        print(f"Fib number {counter+1}:")
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        counter += 1