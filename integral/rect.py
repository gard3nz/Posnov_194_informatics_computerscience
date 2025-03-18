import math
import time

start_time = time.time()
for i in range(0, 1000):
    a = 0
    b = 1
    n = 10000
    h = (b - a) / n
    sum = 0
    for i in range(n):
        x_i = a + i * h
        sum += x_i * x_i + math.sin(x_i)
    integral = sum * h
    a = 0
    b = 1
    n = 10000
    h = (b - a) / n
    sum = 0.5 * ((a * a + math.sin(a)) + (b * b + math.sin(b)))
    for i in range(1, n):
        x_i = a + i * h
        sum += x_i * x_i + math.sin(x_i)
    integral = sum * h
end_time = time.time()
print("Результат интегрирования методом прямоугольников:", integral)
print("Результат интегрирования методом трапеций:", integral)
worktime = end_time - start_time
print("Время на выполнение программы: ", worktime)
