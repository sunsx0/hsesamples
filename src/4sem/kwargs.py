def enum(v):
    i = 0
    for x in v:
        yield i, x
        i += 1


def print_args(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    for i, arg in enum(args):
        print(f'[{i}] = {arg}')
    for key, arg in kwargs.items():
        print(f'{key} = {arg}')


print_args(1, 2, 3, a=1, b=2, c=3)


def magic():
    yield 1
    print('1 yielded')
    yield 2
    print('2 yielded')


for value in magic():
    print('value', value)
    if value == 2:
        break
