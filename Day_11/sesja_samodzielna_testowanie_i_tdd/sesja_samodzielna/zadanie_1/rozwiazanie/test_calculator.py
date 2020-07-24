import unittest

from sesja_samodzielna.zadanie_1.rozwiazanie.calculator import Calculator


class TestCalculator(unittest.TestCase):
    A = 5
    B = 2

    def setUp(self) -> None:
        self.calculator = Calculator(self.A, self.B)

    def test_initial_params(self):
        a_expected = self.A
        b_expected = self.B

        a_result = self.calculator.a
        b_result = self.calculator.b

        self.assertEqual(a_result, a_expected)
        self.assertEqual(b_result, b_expected)

    def test_add(self):
        expected = self.A + self.B

        result = self.calculator.add()

        self.assertEqual(result, expected)

    def test_mul(self):
        expected = self.A * self.B

        result = self.calculator.mul()

        self.assertEqual(result, expected)

    def test_sub(self):
        expected = self.A - self.B

        result = self.calculator.sub()

        self.assertEqual(result, expected)

    def test_sub_with_reverse(self):
        expected = self.B - self.A

        result = self.calculator.sub(reverse=True)

        self.assertEqual(result, expected)

    def test_div(self):
        expected = self.A / self.B

        result = self.calculator.div()

        self.assertEqual(result, expected)

    def test_div_with_reverse(self):
        expected = self.B / self.A

        result = self.calculator.div(reverse=True)

        self.assertEqual(result, expected)

    def test_div_raises_zero_division_error(self):  # dla chetnych
        calculator_with_zero_values = Calculator(0, 0)
        with self.assertRaises(ZeroDivisionError):
            calculator_with_zero_values.div()
