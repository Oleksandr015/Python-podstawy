from Day_10_MOCKI.wallet import Wallet


class Owner:

    def __init__(self, first_name, last_name, wallet: Wallet):
        self.first_name = first_name
        self.last_name = last_name
        self._wallet = wallet

    def supply_wallet(self, cash):
        self._wallet.add_cash(cash)

    def withdraw_money(self, amount):
        self._wallet.spend_cash(amount)

    def check_if_can_afford(self, amount):
        if self._wallet.get_balance() < amount:
            return False
        else:
            return True


