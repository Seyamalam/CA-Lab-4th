def fibonacci_sequence(n):
    if n < 0:
        return []
    fibo_series = [0] * (n + 1)
    if n >= 0:
        fibo_series[0] = 0
    if n >= 1:
        fibo_series[1] = 1

    for i in range(2, n + 1):
        fibo_series[i] = fibo_series[i - 1] + fibo_series[i - 2]

    return fibo_series


n = int(input("Enter the number: "))
print(f"The Fibonacci numbers up to {n} are: {fibonacci_sequence(n)}")
