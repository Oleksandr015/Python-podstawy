"""
ZADANIE 3

Treść w pliku testowym test_tdd_sample.py

"""


def func(number):
    change_string = str(number)
    new_number = int(change_string[::2])
    return new_number * 2

if __name__ == '__main__':
    print(func(19023))