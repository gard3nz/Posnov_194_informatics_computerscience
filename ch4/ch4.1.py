def scalar(a, b):
    return sum(a[i] * b[i] for i in range(3))

def vector(a, b):
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]

def scalar3(a, b, c):
    sc = scalar(b, c)
    return scalar(a, [sc] * 3)

def vector3(a, b, c):
    vc = vector(b, c)
    return vector(a, vc)

a = [5, 2, 3]
b = [4, 5, 2]
c = [5, 3, 4]
print("Скалярное произведение:", scalar(a, b))
print("Векторное произведение:", vector(a, b))
print("Скалярное смешанное произведение:", scalar3(a, b, c))
print("Векторное смешанное произведение:", vector3(a, b, c))
