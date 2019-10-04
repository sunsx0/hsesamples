a = [
    1, 2, 6, 7, 10,
]
x = 3

ans = (0, 1)
distance = abs(a[1] - a[0] - x)

l = 0
for r in range(1, len(a)):
    v = a[r] - a[l]
    if abs(v - x) < distance:
        distance = abs(v - x)
        ans = (l, r)

    while l + 1 < r and a[r] - a[l] > x:
        l += 1
        d = abs(a[r] - a[l] - x)
        if d < distance:
            distance = d
            ans = (l, r)

print(*ans)
