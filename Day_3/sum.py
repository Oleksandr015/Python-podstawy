'''Napisz funkcję, która przyjmuje  liczbę a zwraca sumę  jej cyfr.'''


def sum_cyfr(cyfra):
    result = 0
    while cyfra > 0:
        result += cyfra % 10
        cyfra = cyfra // 10

    return result
