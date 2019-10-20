import typing


class BaseAnimal:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'<{type(self).__name__}(name={self.name})>'

    @property
    def can_fly(self):
        return False

    @property
    def can_swim(self):
        return False

    def move(self):
        print(f'{self} moved')

    def eat(self):
        print(f'{self} eat')

    def feed(self) -> list:
        raise NotImplementedError()


class Fish(BaseAnimal):
    def move(self):
        print(f'{self} swim')

    @property
    def can_swim(self):
        return True

    def feed(self):
        return [typing.Any]


class Bird(BaseAnimal):
    def move(self):
        print(f'{self} fly')

    @property
    def can_fly(self):
        return True

    def feed(self):
        return [Fish]

f = Fish(name='nemo')
b = Bird(name='gosha')

print(f)
print(b)
