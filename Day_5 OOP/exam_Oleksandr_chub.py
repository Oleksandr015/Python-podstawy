"""
1. Napisz funkcję power przyjmującą dwie liczby jako argumenty i zwracającą
   potęgę pierwszej liczby do drugiej.
​
2. Napisz funkcję odd_square, która przyjmuje listę liczb całkowitych a zwracająca
   kwadraty tych liczb, które są parzyste.
​
3. Napisz funkcję count_positive która przyjmuje listę liczb i zwraca liczbę liczb większych
   od zera znajdujących się na tej liście.
​
4. Napisz funkcję equal_indexes, która przyjmuje dwie listy takiej samej długości a zwraca indeksy
   pod którymi odpowiadające sobie elementy na listach mają taką samą wartość.
​
5. Napisz funkcję build_dict, która przyjmuje dwie listy a z nich buduje słownik, w którym
   kluczami są elementami DRUGIEJ listy a wartościami elementy PIERWSZEJ listy.
​
6. Napisz funkcję crazy_dicts, która przyjmuje słownik par napis: liczba (str: int) i wykonuje:
   - Pozostawia w słowniku tylko te klucze, którzych długość jest większa od 2
   - Pozostawia w słowniku tylko te klucze dla których wartość jest dodatnia
   - Odwraca klucze z wartościami.
"""


def power(a, b):
    return a ** b


def odd_square(values):
    return [value ** 2 for value in values if value % 2 == 1]


def count_positive(values, value=None):

    return len([value  for value in values if value > 0])


def equal_indexes(first_list, second_list):
    return [index for index, (value_1, value_2) in enumerate(zip(first_list, second_list)) if value_1 == value_2]



def build_dict(first_list, second_list):
    return {key: value for key, value in zip(second_list, first_list)}


def crazy_dicts(dictionary):
    return {value: key for key, value in dictionary.items() if len(key) > 2 and value > 0}


def evaluate(task, expected_results, arguments, counter):
    print(f'\nTask: {task.__name__}')
    points = 0
    for expected, kwargs in zip(expected_results, arguments):
        received = task(**kwargs)
        point = int(received == expected)
        points += point
        print(f'Expected {expected}, received: {received}, point: {point}')
    print(f'Result: {points} / {len(expected_results)}')
    counter.update(points, len(expected_results))
    return points, len(expected_results)


class PointsCounter:
    def __init__(self):
        self.points = 0
        self.max_points = 0

    def update(self, a, b):
        self.points += a
        self.max_points += b

    def __str__(self):
        return f'Points: {self.points} / {self.max_points}'


if __name__ == '__main__':
    counter = PointsCounter()

    evaluate(power, [1, 1024],
             [{'a': 2, 'b': 0}, {'a': 2, 'b': 10}], counter)
    evaluate(odd_square, [[], [9, 49]],
             [{'values': [2, 4, 8]}, {'values': [0, 3, 2, 2, 4, 8, 7]}], counter)

    evaluate(count_positive, [0, 3],
             [{'values': [-1, -2, -3]}, {'values': [-1, 3, 2, 9]}], counter)

    evaluate(equal_indexes, [[0, 3], [1, 2]],
             [{'first_list': [-1, -2, -3, 4], 'second_list': [-1, 0, 0, 4]},
              {'first_list': [9, 0, 2], 'second_list': [0, 0, 2]}], counter)

    evaluate(crazy_dicts, [{5: 'dddd'},
                           {1: 'bbb', 21: 'ccc'}],
             [{'dictionary': {'a': 1, 'bb': -1, 'ccc': -1, 'dddd': 5}},
              {'dictionary': {'aaaa': -9, 'bbb': 1, 'ccc': 21, 'dddd': -5}}], counter)

    evaluate(build_dict, [{'a': 1, 'b': 2}, {(1, 1): 'Ala', 'Bob': 12}],
             [{'first_list': [1, 2], 'second_list': ['a', 'b']},
              {'first_list': ['Ala', 12], 'second_list': [(1, 1), 'Bob']}], counter)

    print()
    print('Final result: ')
    print(counter)
