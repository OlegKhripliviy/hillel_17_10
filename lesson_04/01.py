from typing import Generator
from uuid import NAMESPACE_DNS, UUID, uuid3, uuid4


class User:
    def __init__(self, id_: UUID, name: str) -> None:
        self.id_: UUID = id_
        self.name: str = name

    def __str__(self) -> str:
        return f"uuid4:\n{self.id_}, {self.name}"


john = User(id_=uuid4(), name="John")
mary = User(id_=uuid4(), name="Mary")

print(john)
print(mary)


# _____________________________________________________________________________________________________________________


def get_id(value: str) -> UUID:
    return uuid3(NAMESPACE_DNS, value)


class User1:
    def __init__(self, username: str) -> None:
        self.id_: UUID = get_id(username)
        self.username: str = username

    def __str__(self) -> str:
        return f"uuid3:\n{self.id_}, {self.username}"


john1 = User1(username="John")
mary1 = User1(username="Mary")
another_john = User1(username="John")

print(john1)
print(mary1)
print(another_john)


# _____________________________________________________________________________________________________________________


def create_random_uuid() -> Generator:
    data = set()
    while True:
        new_value: UUID = uuid4()
        if new_value in data:
            continue
        else:
            data.add(new_value)
        yield new_value


random_uuid: Generator = create_random_uuid()


class User2:
    def __init__(self, username: str) -> None:
        self.id_: UUID = next(random_uuid)
        self.username: str = username

    def __str__(self) -> str:
        return f"uuid4 generator:\n{self.id_}, {self.username}"


john2 = User2(username="John")
mary2 = User2(username="Mary")
another_john2 = User2(username="John")

print(john2)
print(mary2)
print(another_john2)
