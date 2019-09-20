a = int(input())
b = int(input())

a_max = (2 * a) // (a + b + 1) * a
b_max = (2 * b) // (a + b) * b

print(a_max + b_max)
