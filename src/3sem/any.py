s = '234242'
s2 = '0' + s[1:]
print(s2)


s = 'AbCdEf'
print(s.lower())

e = 'abc@gmail.com'
login, _, domain = e.partition('@g')
print(login, _, domain)

e = 'nfckwnfw'
login, _, domain = e.partition('@')
print(login, _, domain)

print('SPLIT WITH PARTITION:')
s = 'acsccs;cdscs;ssdcsdcs'  # ;
while s:
    value, _, s = s.partition(';')
    print(value)

print('TUPLE: ', id((1, 'a')) == id((1, 'a')))


print('SPLIT WITH PARTITION v2:')
s = 'acsccs;cdscs;ssdcsdcs'  # ;
a = []
while s:
    a.append(s.partition(';'))
    s = a[-1][-1]
print(a)

print('SPLIT:')
s = ' acsccs;cdscs;;ssdcsdcs'  # ;
a = s.split(';')
print(a)

print(s.split(';', maxsplit=1))

print('STRIP:')
s = ' acsccs \n   '  # ;
print(s.strip())
print(s.strip('sc '))

print('CONTAINS:')
s = 'abcacb'
s2 = 'ca'
s3 = 'g'
print(s2 in s, s3 in s)
print(s.find(s2) >= 0, s.find(s3) >= 0)
print(s.count(s2) > 0, s.count(s3) > 0)

print('FIND ALL')
s = 'acbfd3ecbcwcacbacacb'
t = 'ac'
a = []
offset = 0
while offset >= 0:
    offset = s.find(t, offset)
    if offset >= 0:
        a.append(offset)
        offset += 1
print(a)
print(s.count(t))

print('FILTER STR:')
s = 'wnfkn  kj34k D jsknf w'
s2 = ''.join(
    ch
    for ch in s
    if ch.isalnum() and ch.islower()
)
s3 = ''.join(
    ch
    if ch.isalnum() and ch.islower() else
    '_'
    for ch in s
)
print(s2)
print(s3)

print('23424324'.isnumeric())
print('abcwdew njwfnkew'.title())
