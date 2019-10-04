a = [1, 4, 5, 7, 19, 24]
b = [4, 6, 7, 18, 24, 134]

i = 0
j = 0
ans = []
while i < len(a) or j < len(b):
    if j == len(b) or (i < len(a) and a[i] < b[j]):
        ans.append(a[i])
        i += 1
    else:
        ans.append(b[j])
        j += 1

print(*ans)
