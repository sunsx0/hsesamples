v = [1, 4, 2, 6, 2, 6]
k = 10

# O(k + n)
v.reverse()
for i in range(k):
    v.append(i)
v.reverse()

# O((k + n) ^ 2)
# for i in range(k):
#     v.insert(0, i)

print(*v)
