a = {1: '1', 2: '10', 3: '11'}
a = {
    k: v
    for k, v in a.items()
    if len(v) == 2
}
print(a)

items = list(a.items())
print(items)
d = dict(items)
print(d)
