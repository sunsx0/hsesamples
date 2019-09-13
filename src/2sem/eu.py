a = int(input())
b = int(input())

while a:
    b %= a
    a, b = b, a

print(b)
