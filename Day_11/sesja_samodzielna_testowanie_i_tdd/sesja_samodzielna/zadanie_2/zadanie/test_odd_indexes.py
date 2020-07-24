import unittest

from Day_11.sesja_samodzielna_testowanie_i_tdd.sesja_samodzielna.zadanie_2.zadanie.odd_indexes import odd_indexes


class TestOddIndexes(unittest.TestCase):


    def test_get_odd_numbers(self):
        test_input = 'komputer'
        expected = 'optr'
        result = odd_indexes(test_input)
        self.assertEqual(expected, result)

    def test_empty_string(self):
        test_input = ''
        expected = ''
        result = odd_indexes(test_input)
        self.assertEqual(expected, result)

    def test_one_character(self):
        test_input = 'u'
        expected = ''
        result = odd_indexes(test_input)
        self.assertEqual(expected, result)

    def test_empty_string(self):
        test_input = 123
        expected = '2'
        result = odd_indexes(test_input)
        self.assertEqual(expected, result)