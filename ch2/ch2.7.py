r = int(input())
print("Диаметр: " + str(r * 2))

sm = 0
for i in range(100, 501):
    sm += i
print("Сумма всех целых чисел от 100 до 500: " + str(sm))

sum = 0
a = int(input())
if a < 500:
    for i in range(a, 501):
        sum += i
    print("Сумма всех целых чисел от " + str(a) + " до 500: " + str(sum))
