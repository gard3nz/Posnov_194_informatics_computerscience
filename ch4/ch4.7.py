def f(n, k):
    c = 0
    a = k
    while a <= n:
        c += n // a
        a *= k
    return c
print(f(10,2))
