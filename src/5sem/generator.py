import math


def read_lines(f=None, until=None):
    if f is None:
        f = lambda x: x
    if until is None:
        until = lambda x: False
    while True:
        s = input()
        if s:
            v = f(s)
            if until(v):
                break
            yield v
        else:
            break

r = read_lines(
    f=lambda x: math.pow(float(x), 2),
    until=lambda x: x == 0,
)
print(sum(r))
