def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)


n = int(input("Enter the number: "))
result = factorial(n)
print(f"The factorial of {n} is {result}")
