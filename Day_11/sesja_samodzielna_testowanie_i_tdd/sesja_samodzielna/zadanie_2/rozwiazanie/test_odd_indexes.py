import unittest

from sesja_samodzielna.zadanie_2.rozwiazanie.odd_indexes import odd_indexes


class TestOddIndexes(unittest.TestCase):

    def test_empty_string(self):
        expected = ''
        empty_str = ''

        result = odd_indexes(empty_str)

        self.assertEqual(result, expected)

    def test_single_character_str(self):
        expected = ''
        single_char_str = 't'

        result = odd_indexes(single_char_str)

        self.assertEqual(result, expected)

    def test_multiple_characters_str(self):
        expected = 'yysbekritz'
        multiple_chars_str = 'Byly sobie kurki trzy'

        result = odd_indexes(multiple_chars_str)

        self.assertEqual(result, expected)

    def test_numeric_input(self):
        expected = '24'
        numeric_input = 1234

        result = odd_indexes(numeric_input)

        self.assertEqual(result, expected)
