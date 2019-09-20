a = 353453
b = 'sedfe'
c = True

s1 = '{} {} {} {c}'.format(a, b, b, c=c)
s2 = '{0} {1} {1} {c}'.format(a, b, c=c)
s3 = f'{a} {b} {b} {c | True}'
print(s1)
print(s2)
print(s3)
