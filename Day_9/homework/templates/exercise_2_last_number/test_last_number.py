import unittest

from Day_9.homework.templates.exercise_2_last_number.last_number import last_number


class TestLastNumber(unittest.TestCase):

    def test_single_digit_number(self):
        single_digit = 6
        expected = 6
        result = last_number(single_digit)
        self.assertEqual(result, expected)

    def test_multiple_digit_number(self):
        multiple_digit = 5645
        expected = 5
        result = last_number(multiple_digit)
        self.assertEqual(result, expected)