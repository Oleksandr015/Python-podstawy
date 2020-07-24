import unittest

from Day_9.templates.exercise_2_last_number.last_number import last_number


class TestLastNumber(unittest.TestCase):

    def test_single_digit_number(self):
        intenger = 1
        expect = 1
        result = last_number(intenger)
        self.assertEqual(result, expect)

    def test_multiple_digit_number(self):
        intenger = 100
        expect = 0
        result = last_number(intenger)
        self.assertEqual(result, expect)
