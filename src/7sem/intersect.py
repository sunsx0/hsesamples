a = [1, 4, 5, 7, 19, 24]
b = [4, 6, 7, 18, 24, 134]

i = 0
j = 0
ans = []
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        ans.append(a[i])
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1

print(*ans)
