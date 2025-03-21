import math
import numpy as np
import time

start_time = time.time()
for i in range(0, 1000):
    a = -3
    b = 3
    n = 10000
    h = (b - a) / n
    def f(x):
        return np.sin(x)**2 - 0.2*np.sin(x) - 0.35
    x = np.arange(-3, 3, h)
    y = f(x)
    integral = np.sum(y * h)
    integral = (np.sum(y) + 0.5 * ((a * a + np.sin(a)) + (b * b + np.sin(b))))*h
end_time = time.time()
print("Результат интегрирования методом прямоугольников:", integral)
print("Результат интегрирования методом трапеций:", integral)
worktime = end_time - start_time
print("Время на выполнение программы: ", worktime)
