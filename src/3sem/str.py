s = '0123456'
rev = s[::-1]
print(rev)

res = ''
i = len(s) - 1
while i >= 0:
    res += s[i]
    i -= 1

print(res)
