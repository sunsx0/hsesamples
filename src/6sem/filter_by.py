import typing


def filter_by(a: typing.List, f: typing.Callable):
    pos = 0
    for v in a:
        if not f(v):
            a[pos] = v
            pos += 1
    while pos < len(a):
        a.pop()


a = [0, 1, 2, 3, 0, 1, 0, 0, 4, 5, 6]
filter_by(a, lambda x: x == 0)
print(*a)
