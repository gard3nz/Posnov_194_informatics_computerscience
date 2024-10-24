pi = 2.0
for i in range(1, 100000):
    left = (2.0 * i)/(2.0 * i - 1.0)
    right = (2.0 * i)/(2.0 * i + 1.0)
    pi = pi * left * right
print(pi)
