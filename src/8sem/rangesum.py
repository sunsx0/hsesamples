def check_range(v, x):
    s = 0
    used = {0}
    for a in v:
        s += a
        if s - x in used:
            return True
        used.add(s)
    return False

a = (-1, 2, -3, 4, 5, 10)
x = -1
print(check_range(a, x))
