from functools import partial, reduce


sum2 = partial(reduce, lambda x, y: x + y)

print(sum((1, 2, 3)))