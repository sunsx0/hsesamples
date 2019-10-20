import typing

import dataclasses as dc


@dc.dataclass
class User:
    login: str = ''
    age: int = 15
    friends: typing.List[str] = dc.field(default_factory=list)


u = User()
u.friends.append('s1')
u2 = User()
u2.friends.append('s1')
print(u.friends)
print(u2.friends)
print(u == u2)

# print(User(login='Ivan', age=14))
# print(User.__annotations__)