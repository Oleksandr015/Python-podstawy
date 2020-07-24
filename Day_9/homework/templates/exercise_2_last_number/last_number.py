"""
LAST NUMBER

Stwórz funckję zwracającą ostatnią cyfrę z podanej liczby. Liczba podawana jest przez parametr 'number'.
Zarówno liczba podawana jak i zwracany wynik musi być typu int.
Napisz testy dla tej funkcji w pliku test_last_number.py.

Wskazówki:
*   aby uzyskać ostatnią cyfrę z liczby bardzo pomocne okazuje się zamienienie typu dostarczonej liczby na string
    za pomocą funkcji str(). Np. str(<liczba>).
*   aby zwracana liczba byla znowu int'em warto użyć funkcji int(). Np. int(<str_liczba>)
*   zalecam operację znajdowania ostatniej cyfry wykonać za pomocą operatora [] z odpowiednim ideksem.
    Np. <str_liczba>[<indeks>]

"""


def last_number(number):
    str_number = str(number)
    return int(str_number[-1])

if __name__ == '__main__':
    print(last_number(5448645))
