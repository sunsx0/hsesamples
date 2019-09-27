def new_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


for i in range(10):
    print(i)

for i in new_range(10):
    print(i)
