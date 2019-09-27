for i in range(0, 10, 2):
    if i == 4:
        continue
    print(i)
    if i == 6:
        break


print(' '.join(map(str, range(10))))

for i in range(100000010000001000000100000010000001000000):
    print(i)
    if i > 10:
        break