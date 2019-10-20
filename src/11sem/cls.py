class Matrix:
    def __init__(self, x: list):
        self.x = x

    def __str__(self):
        return '\n'.join(
            map(
                lambda row: ' '.join(map(str, row)),
                self.x,
            )
        )

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.x[index]
        elif isinstance(index, tuple):
            return self.x[index[0]][index[1]]
        else:
            raise ValueError(f'invalid index')

    @property
    def rows(self):
        return len(self.x)

    @property
    def columns(self):
        return len(self.x[0])

    def __add__(self, other):
        return Matrix(
            [
                [
                    v1 + v2
                    for v1, v2 in zip(row1, row2)
                ]
                for row1, row2 in zip(self.x, other.x)
            ]
        )

    @classmethod
    def identity(cls, n: int):
        return cls.diag(n, 1)

    @staticmethod
    def diag(n: int, value):
        return Matrix(
            [
                [
                    value if i == j else 0
                    for j in range(n)
                ]
                for i in range(n)
            ]
        )
