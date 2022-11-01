from typing import Generator, Iterable

data1 = [1, 2, 3, 4, 1, 4, 5, 32, 42, 34, 1, 34, 54, 43, 21, 23, 43, 22, 24]


def get_list_without_duplicates(data: list) -> list:
    values = set()
    new_data: list = []
    for element in data:
        if element not in values:
            values.add(element)
            new_data.append(element)
    return new_data


filtered = get_list_without_duplicates(data1)

print(f"{data1=}")
print(f"{filtered=}")


# ---------------------------------------------------------------------------------------------------------------------


def deduplication(collection: Iterable) -> Generator:
    values = set()
    for element in collection:
        if element in values:
            continue
        values.add(element)
        yield element


for item in deduplication(data1):
    print(item)


# ---------------------------------------------------------------------------------------------------------------------


class User:
    def __init__(self, username: str, age: int) -> None:
        self.username: str = username
        self.age: int = age

    def __repr__(self) -> str:
        return f"{self.username}, {self.age}"


def only_adults(users: Iterable[User]) -> Generator:
    for user in users:
        if user.age > 18:
            yield user


john = User(username="John", age=22)
mary = User(username="Mary", age=8)

users1 = [john, mary]

print(list(only_adults(users1)))
only_adults = (user for user in users1 if user.age > 18)
print(list(only_adults))
