a = [1, 2, 3, 4]
b = [2, 2, 3, 4]

r = all(x <= y for x, y in zip(a, b))

print(a <= b)
print(r)
