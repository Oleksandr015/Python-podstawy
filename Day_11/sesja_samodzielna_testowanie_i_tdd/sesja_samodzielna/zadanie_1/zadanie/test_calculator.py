import unittest


# Dla chetnych przetestuj wystapienie wyjatku przy dzieleniu przez 0.
from Day_11.sesja_samodzielna_testowanie_i_tdd.sesja_samodzielna.zadanie_1.zadanie.calculator import Calculator


class TestCalculator(unittest.TestCase):
    a = 3
    b = 15

    def setUp(self) -> None:

        self.calculator = Calculator(self.a, self.b)



    def test_sum_two_numbers(self):

        expected = self.a+ self.b
        result = self.calculator.add()
        self.assertEqual(expected, result)


    def test_multiplay_two_numbers(self):

        expected = self.a * self.b
        result = self.calculator.mul()
        self.assertEqual(expected, result)

    def test_sub_function_if_True(self):
        expected = self.b - self.a
        result = self.calculator.sub(True)
        self.assertEqual(expected, result)

    def test_sub_function_if_False(self):
        expected = self.a - self.b
        result = self.calculator.sub(False)
        self.assertEqual(expected, result)

    def test_div_function_if_True(self):
        expected = 5.0
        result = self.calculator.div(True)
        self.assertEqual(expected, result)

    def test_div_function_if_False(self):
        expected = 0.2
        result = self.calculator.div(False)
        self.assertEqual(expected, result)





