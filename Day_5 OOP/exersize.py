"""
Klasa Person
Dwa atrybuty: name, age (imię, wiek)
Dwie funkcje: - introduce: Zwracająca przedstawienie w postaci:
              "Hello, my name is (tutaj imie)"
              - to_hundred Zwracającą liczbę lat która nam pozostała
                           do 100 lat życia
              funkcję __repr__ w odpowiedni sposób :)
blok main:
 - utwórz trzy obiekty klasy person
 - Dodaj je do listy persons
 - W pętli for wywołaj dla każdego obiektu introduce
 - ** Dodaj nową funkcję zwracającą napis w postaci:
    "Hello, my name is (tutaj imie). I have still X years to 100.
    Wykorzystując poprzednio zdefiniowane funkcje.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person({self.name}, {self.age})'

    def introduce(self):
        return f'Hello, my name is {self.name}'

    def to_hundred(self):
        return 100 - self.age

    def stil_to_hundred(self):
        return f'{self.introduce()}. I have {self.to_hundred()} years to 100.'

    def your_age_is_even(self):
        return [person for person in list_persons if person.age % 2 ==0]

if __name__ == '__main__':
    person_1 = Person('Piotr', 25)
    person_2 = Person('Eva', 28)
    person_3 = Person('Ivan', 25)

    print(person_1)
    print(person_1.introduce())
    list_persons = [person_1, person_2, person_3]

    for person in list_persons:
        print(person.introduce())
        print(person.stil_to_hundred())

    print(person_1.your_age_is_even())