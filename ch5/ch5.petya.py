def srav(s1, s2):
    s1_ = s1.lower()
    s2_ = s2.lower()
    if s1_ < s2_:
        return -1
    elif s1_ > s2_:
        return 1
    else:
        return 0
st1 = input()
st2 = input()
print(srav(st1, st2))
