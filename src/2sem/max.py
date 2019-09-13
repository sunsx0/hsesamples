res = None
while True:
    s = input()
    if s == 'c':
        break
    else:
        n = int(s)
        if res is None or n > res:
            res = n
print(res)
