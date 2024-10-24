def f(s):
    words = s.split()
    tag = '#' + ''.join(word.capitalize() for word in words)
    if len(tag) > 140 or len(tag) == 1:
        return False
    return tag
s = str(input())
print(f(s))
