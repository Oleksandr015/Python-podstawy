import unittest

from .wallet import Wallet, InsufficientAmount


class TestWallet(unittest.TestCase):

    def setUp(self) -> None:
        self.wallet_20 = Wallet(20)


    def test_empty_wallet(self):
        wallet = Wallet()
        result = wallet.get_balance()
        self.assertEqual(result, 0, 'empty')

    def test_wallet_wits_cash(self):
        wallet = Wallet()
        result = self.wallet_20.get_balance()
        self.assertEqual(result, 20, "test")

    def test_adding_cash(self):
        wallet = Wallet(40)
        cash = 20

        wallet.spend_cash(cash)
        result = wallet.get_balance()

        self.assertEqual(result, 20)

    def test_spend_cash(self):
        wallet = Wallet(40)
        cash = 20
        wallet.spend_cash(cash)

    def test_exception(self):
        wallet = Wallet(20)
        cash = 30

        with self.assertRaises(InsufficientAmount):
            self.wallet_20.spend_cash(cash)


