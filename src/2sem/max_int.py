a = 1
b = 1

while a is b:
    a += 1
    b += 1

print(a, b)
print(id(a), id(b))