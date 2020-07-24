import unittest

from parameterized import parameterized

from Day_10_MOCKI.exercise_9_tdd_is_prime_number.is_prime_number import is_prime_number, PrimeNumber


class TestIsPrimeNumber(unittest.TestCase):
    NOT_PRIME_NUMBER = [[4], [6], [8], [9]]

    def setUp(self) -> None:
        self.prime_number = PrimeNumber()






    def test_less_or_equal_one_is_false(self):
        number = 1
        self.result = is_prime_number(number)

        self.assertFalse(self.result)


    def test_not_prime_numbers(self, not_number):
        for i in self.NOT_PRIME_NUMBER:
            res = self.prime_number.is_prime_number(i)
            self.assertFalse(res)

    @parameterized.expand([
        [2], [3], [5], [7]
    ])
    def test_prime_numbers(self, prime_number):
        result = is_prime_number(prime_number)
        self.assertTrue(result)
