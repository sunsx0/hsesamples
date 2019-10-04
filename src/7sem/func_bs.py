def f(x):
    return x * x * x

l = 0.0
r = 10.0
t = 6.354
eps = 0.00000000000000000001

while True:
    c = (l + r) / 2
    y = f(c)
    if abs(y - t) < eps:
        l = r = c
        break

    if y < t:
        l = c
    else:
        r = c

print(l, f(l), t)
