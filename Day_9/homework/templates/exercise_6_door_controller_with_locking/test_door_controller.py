import unittest

#DoorController, DoorLockedError
from Day_9.homework.templates.exercise_6_door_controller_with_locking.door_controller import DoorController, \
    DoorLockedError


class TestDoorController(unittest.TestCase):

    def setUp(self) -> None:
        self.door_controller = DoorController()

    def test_initially_door_is_closed(self):
        # testowac to ze drzwi po utworzeniu sa zamkniete
        result = self.door_controller.is_door_opened()
        self.assertFalse(result)

    def test_open_door(self):
        # testowac czy drzwi po utwarciu sie otwarte
        self.door_controller.open()  # otwarte
        result = self.door_controller.is_door_opened()  # -> True
        self.assertTrue(result)

    def test_close_door(self):  # tu ostrożnie - pamiętajmy, że drzwi domyślnie są zamknięte
        # testowac czy drzwi po zamknieciu sa zamkniete

        self.door_controller.open()  # otwarte
        door_opened = self.door_controller.is_door_opened()
        self.assertTrue(door_opened)

        self.door_controller.close()  # zamkniete
        door_closed = self.door_controller.is_door_opened()
        self.assertFalse(door_closed)

    def test_initially_door_is_not_locked(self):
        # sprawdzić czy początkowo drzwi nie są zablokowanie (assertFalse lub assertTrue)
        result = self.door_controller.unlock()
        self.assertFalse(result)

    def test_lock_door_closes_and_locks(self):
        # wazne aby pamietac ze drzwi najpierw musza byc otwarte!!!
        # testujemy czy drzwi po lock() są zamkniete i zablokowane
        self.door_controller.open()  # otwarte

        result = self.door_controller.lock()  # -> True
        self.assertTrue(result)


    def test_unlock_door(self):
        # aby można było odblokowac drzwi muszą byc one najpierw zablokowane!!!
        self.door_controller.lock()
        result = self.door_controller.unlock()
        self.assertFalse(result)

    def test_exception_on_opening_locked_doors(self):
        # Testujemy wystąpienie wyjątku. Polecam sprawdzić w prezentacji składnię!
        # Użyć rozwiązania z context managerem 'with'
        # Pamietaj ze trzeba zaimportowac wyjatek DoorLockedError
        # Pamietajmy ze najpierw musimy zablokowac drzwi, a potem dopiero probowac je otwierac
        self.door_controller.lock()
        with self.assertRaises(DoorLockedError, msg="DoorLockedError"):
            self.door_controller.open()


# def test_spend_cash_raises_exception_on_insufficient_amount(self):
#        cash = 10
#        with self.assertRaises(InsufficientAmount, msg='Not raised on spending more money than available'):
#            self.empty_wallet.spend_cash(cash)
