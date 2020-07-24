import unittest

from Day_9.homework.templates.exercise_4_guest_list.guest_list import GuestList


class TestGuestList(unittest.TestCase):

    def setUp(self) -> None:
        self.guest_list = GuestList()

    def test_get_guest_list_is_empty(self):  # przypadek gdy lista jest pusta
        result = 'The list is empty'
        expected = self.guest_list.get_guest_list()
        self.assertEqual(expected, result)

    def test_add_list_adds_person(self):
        person = 'Leonardo DiCaprio'
        result = [person]
        self.guest_list.add_guest(person)
        expected = self.guest_list.get_guest_list()
        self.assertEqual(result, expected)

    def test_added_person_is_invited(self):  # test dla is_person_invited() równego True
        person = "Alek"
        self.guest_list.add_guest(person)
        result = [person]
        expected = self.guest_list.is_person_invited(person)
        self.assertTrue(result)



    def test_added_person_is_not_invited(self):  # test dla is_person_invited() równego False
        person = 'Aleksandr'
        other_person = 'Oleksandr'
        self.guest_list.add_guest(person)
        result = self.guest_list.is_person_invited(other_person)
        self.assertFalse(result)

