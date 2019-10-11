from collections import defaultdict

def magic():
    print('magic')
    return 0

d = defaultdict(magic)

d['request'] += 1
d['request'] += 1
d['test'] += 2

print(d)
