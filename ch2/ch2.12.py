def b(kb):
    return kb * 1024
def kb(b):
    return b / 1024
print("Введите число:")
num = int(input())
print("1 - перевести в килобайты, 2 - перевести в байты)")
a = input()
if a == "1":
    print("Результат в КБ: " + str(kb(num)))
else:
    print("Результат в Б: " + str(b(num)))
