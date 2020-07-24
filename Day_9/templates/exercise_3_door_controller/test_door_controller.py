import unittest


from Day_9.templates.exercise_3_door_controller.door_controller import DoorController


class TestDoorController(unittest.TestCase):

    def setUp(self) -> None:
        self.door_controller = DoorController()

    def test_initially_door_is_closed(self):
        result = self.door_controller.is_door_opened()
        self.assertFalse(result)


    def test_open_door(self):
        self.door_controller.open()
        result = self.door_controller.is_door_opened()
        self.assertTrue(result)

    def test_close_door(self):
        self.door_controller.open()
        door_opened = self.door_controller.is_door_opened()
        self.assertTrue(door_opened)
        self.door_controller.close()
        result = self.door_controller.is_door_opened()
        self.assertFalse(result)
