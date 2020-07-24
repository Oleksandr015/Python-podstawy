import unittest

from parameterized import parameterized

from Day_11.sesja_samodzielna_testowanie_i_tdd.sesja_samodzielna.zadanie_2.zadanie.odd_indexes import odd_indexes


class TestOddIndexes(unittest.TestCase):


    @parameterized.expand([
        ['Tatata'], ['papapam'], ['aaaaaa']
    ])
    def test_empty_string(self, add_string):

        expected = 'aaa'
        result = odd_indexes(add_string)
        self.assertEqual(expected, result)
