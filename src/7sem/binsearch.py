a = [
    1, 2, 3, 6, 10, 14,
]
t = 10

l = 0
r = len(a) - 1

while l != r:
    c = (l + r) // 2

    if a[c] < t:
        l = c + 1
    elif a[c] > t:
        r = c - 1
    else:
        r = l = c

print(l, r, a[l], a[r])
