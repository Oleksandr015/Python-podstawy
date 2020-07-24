from typing import Tuple, List, Dict


def square_two_number(number_1: int, number_2: int) -> Tuple[int, int]:
    return number_1 ** 2, number_2 ** 2


def power(a: int, b: int) -> int:
    return a ** b


def join_words(words: List[str], separator: str) -> str:
    return separator.join(words)


class Person:
    def __init__(self, name: str, age: int, phone_book: Dict[str, int]):
        self.name: str = name
        self.age: int = age
        self.phone_book: Dict[str, int] = phone_book


def is_person_adult(person: Person) -> bool:
    return person.age >= 18


def get_adults(persons: List[Person]) -> List[Person]:
    return [person for person in persons if is_person_adult()]


if __name__ == '__main__':
    number: float = 12.7
    number_2: int = 5
    name: str = 'Ala'

    print(name)
    name = '12'
    print(name)
    print(square_two_number(5, 6))
    # print(square_two_number("Ala", 6))

    print(join_words(['Ala', 'ma', 'kota'], '--**--'))
    person_1 = Person('Piotr', 25, {'a': 1, 'b': 2})
    person_2 = Person('Ewa', 17, {'a': 1, 'b': 2})
    print(person_1)
    print(person_2)
    print([person_1, person_2])
