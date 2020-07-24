"""

IS PRIME NUMBER

To zadanie ma imitować programowanie przy użyciu TDD. W pliku test_is_prime_number.py znajdują się testy dla funkcji
is_prime_number(number). Na podstawie tych testów należy stworzyć ciało funkcji is_prime_number(number). Specyfikację
należy odczytać z testów.

Wskazówka:
Prime number (liczba pierwsza) to liczba będąca większa od 1, która dzieli się tylko przez 1 oraz samą siebie.

"""
class PrimeNumber:
    def __init__(self):


    def is_prime_number(number):
        if number <= 1:
            return False
        else:
            d = 2
            while d * d <= number and number % d != 0:
                d += 1
            return d * d > number


if __name__ == '__main__':
    print(is_prime_number(7))

#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]