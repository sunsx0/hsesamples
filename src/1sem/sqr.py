import math

print('a * x * x + b * x * c == 0 solution')
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

d = b ** 2 - 4 * a * c

print(
    f'{-b / (2 * a)}'
    if d == 0 else
    f'{(-b + math.sqrt(d)) / (2 * a)} and {(-b - math.sqrt(d)) / (2 * a)}'
    if d > 0 else
    'no solution'
)
