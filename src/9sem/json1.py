import json


FILE = 'test.json'


d = {
    'k': 1,
    't': True,
}


with open(FILE, 'w') as f:
    json.dump(d, f, sort_keys=True)
with open(FILE) as f:
    b = json.load(f)


print(d == b)
print(d)
print(b)
