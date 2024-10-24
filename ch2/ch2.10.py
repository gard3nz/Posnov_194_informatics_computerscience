f = int(input())
s = int(input())
print(f, s)
f, s = s, f
print("После смены: " + str(f) + ", " + str(s))
