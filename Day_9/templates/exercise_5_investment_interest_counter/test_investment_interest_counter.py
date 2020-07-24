import unittest

from parameterized import parameterized

from exercises.exercise_5_investment_interest_counter.investment_interest_counter import InvestmentInterestCounter, \
    DurationLessThenZero


class TestInvestmentInterestCounter(unittest.TestCase):
    INTEREST_RATE = 0.01
    BALANCE = 10000

    def setUp(self) -> None:
        self._interest_counter = InvestmentInterestCounter(self.INTEREST_RATE, self.BALANCE)

    @parameterized.expand([
        [2, 10201],
        [1, 10100]
    ])
    def test_yearly_capitalization(self, duration, expected_balance):  # parametry testowe juz są podane
        pass

    def test_yearly_capitalization_raises_exception(self):
        pass
