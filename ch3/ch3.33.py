def dbl(n):
    if n % 2 == 0:
        product = 1
        for i in range(1, n // 2 + 1):
            product *= (2 * i)
    else:
        product = 1
        for i in range(1, (n + 1) // 2 + 1):
            product *= (2 * i - 1)
    return product
nech = 7
ch = 8
nech_dbl = dbl(nech)
ch_dbl = dbl(ch)
print(f"Двойной факториал {nech}!!: {nech_dbl}")
print(f"Двойной факториал {ch}!!: {ch_dbl}")
