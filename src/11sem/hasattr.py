class Base:
    def __init__(self, x):
        self.x = x


class Value1(Base):
    def __init__(self, x):
        super().__init__(x)
        self.y = x + 1


class Value2(Base):
    y = 15


def magic(v):
    if hasattr(v, 'y'):
        print(v.y)
    else:
        print('empty')


magic(Value1(10))
magic(Value2(10))
magic(Base(10))