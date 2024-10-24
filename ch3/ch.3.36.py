print("Длина массива:")
c = int(input())
print("Введите числа")
m=[]
for i in range(c):
    b=int(input())
    m.append(b)
maxx = max(m)
a=[]
for i in range(len(m)):
    a.append(m[i] / maxx)
print(a)
