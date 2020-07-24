"""
ZADANIE 2

Masz poniższy kod, który dla zadanego stringa zwraca litery z nieparzystych indeksów, np:
teleturniej -> eeune komputer -> optr

Przetestuj tę funkcję dla argumentu, który będzie stringiem.
Uruchom funkcję przekazując int. Zaobserwuj, co się stało. Napisz testy dla argumentów, które są intem.
Popraw funkcję by działała poprawnie, sprawiając by testy przeszły.

Podpowiedz!
Funkcja str() pozwala zamienić element przekazany do niej na string.


ZADANIE 2B

Przepisz testy tak aby używały parametryzcji - dekoratora parametryzacji @parameterized.expand.

"""


def odd_indexes(string):
    new_string = str(string)
    return new_string[1::2]
