"""

ZADANIE 1

Stwórz klasę Calculator, w której zaimplementujesz działania: dodawanie, odejmowanie, mnożenie, dzielenie. Napisz testy,
które przetestują wcześniej wymienione metody.

Specyfikacja:
*   konstruktor jako parametry przyjmuje dwie liczby i zapisuje w atrybutach: self.a, self.b.
*   metoda add() dodaje i zwraca wynik
*   metoda sub() odejmuje liczby od siebie i zwraca wynik. Posiada parametr reverse domyślnie równy False.
    Gdy reverse == False -> self.a - self.b. Gdy reverse == True -> self.b - self.a.
*   metoda mul() mnoży liczby i zwraca wynik
*   metoda div() dzieli liczby i zwraca wynik. Podobnie jak sub() posiada parametr domyślny reverse, który zapewnia
    podobne działanie

"""


class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self, reverse=False):
        if not reverse:
            return self.a - self.b
        else:
            return self.b - self.a

    def mul(self):
        return self.a * self.b

    def div(self, reverse=False):
        if reverse:
            return self.b / self.a
        else:
            return self.a / self.b


if __name__ == '__main__':
    calculate = Calculator(3, 15)
    print(calculate.add())
    print(calculate.mul())
    print(calculate.sub(True))
    print(calculate.div(True))
