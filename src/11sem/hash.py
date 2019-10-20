class Value:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return str(self.x)

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        return self.x == other.x

    def __call__(self, y):
        return self.x + y


v1 = Value(1)
v2 = Value(1)

s: set = {v1, v2}
print(s)
print(v1 == v2)
