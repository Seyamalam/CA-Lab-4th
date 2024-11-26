def sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    return n + sum_of_natural_numbers(n - 1)


n = int(input("Enter the range: "))
result = sum_of_natural_numbers(n)
print(result)
