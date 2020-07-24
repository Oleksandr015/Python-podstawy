"""
ZADANIE 4

Masz dany kod poniżej i plik test2.txt o zawartości: 123456789

Funkcja get_avg pobiera z pliku how_much cyfr i liczy z nich średnią.
Przetestuj funkcję get_avg, wiedząc że w pliku możesz spodziewać się tylko liczb i nie możesz do testów używać pliku.


Podpowiedź!
Potrzebujesz zamockować funkcję _get_data().

"""


def _get_data(how_much):
    with open('test2.txt', 'r') as f:
        return f.read(how_much)


def get_avg(how_much):
    data = _get_data(how_much)
    numbers = [int(x) for x in data]
    return sum(numbers) / len(numbers)


if __name__ == '__main__':
    print(get_avg(3))
