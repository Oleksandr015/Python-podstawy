import unittest

from Day_9.templates.exercise_4_guest_list.guest_list import GuestList


class TestGuestList(unittest.TestCase):

    def setUp(self) -> None:
        self.guest_list = GuestList()

    def test_get_guest_list_is_empty(self):  # przypadek gdy lista jest pusta
        result = self.guest_list.get_guest_list()
        expect = 'The list is empty'
        self.assertEqual(result, expect)

    def test_add_list_adds_person(self):
        person = 'Alek'
        expect = ['Alek']
        self.guest_list.add_guest(person)
        result = self.guest_list.get_guest_list(person)
        self.assertEqual(result, expect)


    def test_added_person_is_invited(self):  # test dla is_person_invited() równego True
        person = "Olek"
        self.guest_list.add_guest(person)

        result = self.guest_list.is_person_invited(person)
        self.assertTrue(result)



    def test_added_person_is_not_invited(self):  # test dla is_person_invited() równego False
        person = "Oleksandr"
        not_invited_person = "Han"
        self.guest_list.add_guest(person)
        result = self.guest_list.is_person_invited(not_invited_person)
        self.assertFalse(result)

