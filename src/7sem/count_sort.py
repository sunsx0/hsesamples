a = [5, 5, 2, 6, 1, 6, 7, 8]
m = max(a)

v = [0] * (m + 1)
for x in a:
    v[x] += 1

ans = []
for i, c in enumerate(v):
    for _ in range(c):
        ans.append(i)

print(*ans)
