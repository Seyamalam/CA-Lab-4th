def split_half(m, n):
    d = (m + n) // 2
    if m == n and n == d:
        return m ** 2
    return split_half(m, d) + split_half(d + 1, n)


result = split_half(2, 4)
print(f"Final Result: {result}")
