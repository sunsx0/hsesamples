def insert_batch(a: list, values: list):
    n = len(a)
    k = len(values)
    for _ in range(k):
        a.append(None)
    i = n - 1
    while i >= 0 and values:
        t, v = values[-1]
        if t > i:
            values.pop()
        else:
            t, v = i, a[i]
            i -= 1
        a[t + len(values)] = v

    for i, v in values:
        a[i] = v


a = [1, 4, 2, 5, 7]
b = [(0, 2), (2, 1), (5, 2)]
insert_batch(a, b)
print(*a)