from functools import reduce
from itertools import chain


def chain2(*iterators):
    print('chain2 enter')
    for it in iterators:
        yield from it
    print('chain2 exit')

a = map(str, range(0, 10, 2))
b = map(str, range(10, 20, 3))
c = chain2(a, b, ('-1', '-2'))

# print('reduce s1')
# s1 = reduce(lambda x, y: f'{x} {y}', c, '')
# print('reduce s2')
# s2 = reduce(lambda x, y: f'{x} {y}', c, '')

# print(s1)
# print(s2)
print(' '.join(c))


with open('sum.py') as f:
    lines = reduce(
        lambda x, y: f'{x}\n{y}',
        map(
            lambda v: v.strip('\n'),
            f,
        ),
    )
    print(lines)
