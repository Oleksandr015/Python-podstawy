# 1. Napisz program tak, aby na ekranie zostało wypisane: "Witaj, świecie!"

print('"Witaj, świecie!"')
print()

# 2. Zmień poprzedni program tak, aby na ekranie zostało wypisane:
# "Witaj, świecie!
# To mój pierwszy program.”

print('"Witaj, świecie!\nTo mój pierwszy program."')
print()


# 3. Napisz funkcję is_even przyjmująca jeden argument zwracającą True w przypadku gdy przekanaza liczba jest parzysta,
# w przeciwnym razie False.

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_even(0))

print()


# 4. Napisz funkcję is_odd przyjmująca jeden argument zwracającą True w przypadku gdy przekanaza liczba jest nieparzysta,
# w przeciwnym razie False.

def is_odd(number_1):
    if number_1 % 2 != 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_odd(0))

print()
# 5. Jaki typu danych potrzebujemy żeby przechowywać PESEL?

print('int')

print()

# 6. Stwórz zmienną do której zapiszesz wynik działania: 4*27

multipl = 4 * 27
print(multipl)

print()
# 7. Stwórz zmienną do której zapiszesz wynik działania: 31/5

division = 31 / 5
print(division)
print()

# 8. Wypisz na ekran wynik sprawdzenia czy liczba 10 jest równa liczbie 5.

x = 10
y = 5
try:
    x = y
except:
    print("Two numbers are not equal")

# 9. Napisz program, w którym tworzysz zmienną, do której przypiszesz swój
# PESEL. (Wczytasz go od użytkownika za pomocą funkcji input). Następnie, jeżeli jest on parzysty, wypisz na ekran: "Twój PESEL
# jest parzysty", a jeżeli jest nieparzysty, to wypisz na ekran: "Twój PESEL
# jest nieparzysty".

def add_pesel(your_code):
    if your_code % 2 == 0:
        print('"Twój PESEL jest parzysty"')
    else:
        print('"Twój PESEL jest nieparzysty"')

if __name__ == '__main__':
    add_pesel(int(input()))

# 10. Napisz program, który wczyta od użytkownika jego imię oraz wiek a następnie napisz i wywołaj funkcję, która przyjmuje imię oraz wiek a zwraca formatowany napis w postaci:
#   "Hello James! Your age 25 is odd!" Zakładając, że użytkownik podał wartości "James" oraz 25.

name, age = map(str, input().split())

print(f"Hello, {name}! Your age is {age} old!")