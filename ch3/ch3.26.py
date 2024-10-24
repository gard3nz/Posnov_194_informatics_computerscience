def wallis_formula(n):
    product = 1.0
    for i in range(1, n + 1):
        product *= (4 * i**2) / (4 * i**2 - 1)
    return 2 * product
n = 100000
pi_approximation = wallis_formula(n)
print(f"Приближенное значение π с использованием {n} членов: {pi_approximation}")
