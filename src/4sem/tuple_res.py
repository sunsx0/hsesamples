def min_max(a, b):
    return min(a, b), max(a, b), 1, 2


a, b = 32, 1
a, b, *_ = min_max(a, b)

print(a, b, _)
