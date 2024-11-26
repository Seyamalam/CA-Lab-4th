def going_down(m, n):
    if m == n:
        return n ** 2
    return (n ** 2) + going_down(m, n - 1)


result = going_down(2, 4)
print(f"Final Result: {result}")
