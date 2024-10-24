def t(st,num):
    s=1
    for i in range(st):
        s=num**s
    return len(str(s))
print(t(3,5))
print(t(5,2))
