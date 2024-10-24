print("Введите своё имя:")
name = input()
print("Введите свой возраст:")
age = int(input())
if age<100:
    print(name + ", через " + str(100 - age) + " лет Вам будет 100 лет")
else:
    print(name + ", вам уже есть 100 лет")
