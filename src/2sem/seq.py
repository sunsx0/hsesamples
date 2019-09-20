last = int(input())
up = True
down = True
cur = 1
ans = 1
while True:
    v = int(input())
    up &= v >= last
    down &= v <= last
    if not up and not down:
        up = v >= last
        down = v <= last
        cur = 2
        ans = max(cur, ans)
    else:
        cur += 1
        ans = max(cur, ans)
    last = v
print(ans)
