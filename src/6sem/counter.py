def iterate(
    ranges: list,
    counter: list = None,
    depth: int = 0,
):
    if counter is None:
        counter = [0] * len(ranges)
    if depth == len(ranges):
        yield counter
        return
    for i in range(ranges[depth]):
        counter[depth] = i
        yield from iterate(ranges, counter, depth + 1)


logins = ['a', 'b', 'c']
passwords = ['x', 'y']
for i, j in iterate((len(logins), len(passwords))):
    print(f'{logins[i]}:{passwords[j]}')
