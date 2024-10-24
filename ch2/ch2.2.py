km = int(input())
m = int(input())
if km * 1000 < m:
    print("Расстояние в км меньше и равно:" + str(km) + "км")
else:
    print("Расстояние в м меньше и равно:" + str(m) + "м")
