"""
ZADANIE 3

Masz test poniżej. Napisz fukcję func, która spełni ten test.

Podpowiedzi:
*   zauważ dwa pierwsze przykłady, druga cyfra argumentu nie ma znaczenia
*   zauważ trzeci przykład, wynikiem jest podwojona wartość argumentu
*   zauważ czwarty przykład, wynikiem jest 13 * 2

"""

import unittest

from parameterized import parameterized

from sesja_samodzielna.zadanie_3.rozwiazanie.tdd_sample import func


class TestTDDSAmple(unittest.TestCase):

    @parameterized.expand([
        (12, 2), (11, 2), (2, 4), (123, 26), (92, 18), (79, 14), (19023, 206)
    ])
    def test_func(self, number, result):
        self.assertEqual(func(number), result)
