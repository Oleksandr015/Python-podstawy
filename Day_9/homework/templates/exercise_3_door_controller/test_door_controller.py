import unittest

from Day_9.homework.templates.exercise_3_door_controller.door_controller import DoorController


class TestDoorController(unittest.TestCase):

    def setUp(self) -> None:
        self.controller = DoorController()

    def test_initially_door_is_closed(self):

        expected = self.controller.is_door_opened()
        self.assertFalse(expected)


    def test_open_door(self):
        self.controller.open()
        expected = self.controller.is_door_opened()
        self.assertTrue(expected)

    def test_close_door(self):  # tu ostrożnie - pamiętajmy, że drzwi domyślnie są zamknięte
        self.controller.open()
        expected = self.controller.is_door_opened()
        self.assertTrue(expected)

        self.controller.close()
        expected = self.controller.is_door_opened()
        self.assertFalse(expected)

