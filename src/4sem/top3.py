a = (1, 5, 3, 0, 2, 4, 2, 10)


def func(a):
    return -a

lam = lambda a: -a

v1, v2, v3, *other = sorted(a, key=lam)
print(v1, v2, v3)
print(*other)
