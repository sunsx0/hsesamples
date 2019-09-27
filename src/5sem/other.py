x = 10
a = [1, 2, 3, 0, 7, 4, 2, 6, 8, 9, 6]
s1 = sum(
    1
    for i, v1 in enumerate(a)
    for j, v2 in enumerate(a)
    if i < j and v1 + v2 == x
)
s2 = 0
for i, v1 in enumerate(a):
    for j, v2 in enumerate(a):
        if j < i and v1 + v2 == x:
            s2 += 1
print(s1, s2)
