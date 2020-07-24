import unittest

from parameterized import parameterized

from sesja_samodzielna.zadanie_2.rozwiazanie.odd_indexes import odd_indexes


class TestOddIndexes(unittest.TestCase):

    @parameterized.expand([
        ('', ''),
        ('t', ''),
        ('Byly sobie kurki trzy', 'yysbekritz'),
        (1234, '24')
    ])
    def test_odd_indexes(self, param, expected):
        result = odd_indexes(param)

        self.assertEqual(result, expected)
