# 1 2 3 4 5
# [1, 2], [3, 4], [5]

def group_k(seq, size):
    r = []
    for v in seq:
        r.append(v)
        if len(r) == size:
            yield tuple(r)
            r.clear()

a = range(1, 6)  # 1, 2, 3, 4, 5
for x, y in group_k(a, 2):
    print(x + y)