def going_up(m, n):
    if m == n:
        return m ** 2
    return (m ** 2) + going_up(m + 1, n)


result = going_up(2, 4)
print(f"Result: {result}")
