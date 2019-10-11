a = {1: '1', 2: '10', 3: '11'}
a[4] = '100'
a[2] = 'mwlde'
a.setdefault(5, '23')
a.setdefault(2, '23')
print(a[3])
print(a[5])
print(a.get(6))
print(a.pop(5))
print(a.pop(5, None))
print(a)
