import unittest

class Walet()
    def __init__(self) -> int:
        self._balance: int = 20

    def add_cash(self, cash: int) -> int:
        self._balance += cash

    def add_ca