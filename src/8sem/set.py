g = {
    'a': ['b', 'c'],
    'c': ['d', 'b', 'e'],
    'e': ['f'],
}

def dfs(v, u: set):
    if v in u:
        return
    print(v)
    u.add(v)
    for child in g.get(v, ()):
        dfs(child, u)

u = set()
dfs('a', u)
print(u)
print(hash('a') % 17)

MOD = 1000000007
[[] for i in range(MOD)]

def contains(ps, v):
    h = hash(v) % MOD
    if v in ps[h]:
        return True
    return False
