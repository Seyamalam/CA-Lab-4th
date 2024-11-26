def sum_of_odd_squares(n):
    if n <= 0:
        return 0
    return (n ** 2) + sum_of_odd_squares(n - 1)


n = int(input("Enter the range: "))
result = sum_of_odd_squares(n)
print(result)
