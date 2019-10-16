import math

a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 10)

# (X - Y, X - Y)


def l2_distance(a, b):
    s = 0.0
    for i in range(len(a)):
        s += (a[i] - b[i]) ** 2
    return math.sqrt(s)


def l2_distance_zip(a, b):
    s = 0.0
    for x, y in zip(a, b):
        s += (x - y) ** 2
    return math.sqrt(s)


def l2_distance_zip_sum(a, b):
    return math.sqrt(
        sum(
            (x - y) ** 2
            for x, y in zip(a, b)
        )
    )


print(l2_distance(a, b))
print(l2_distance_zip(a, b))
print(l2_distance_zip_sum(a, b))
