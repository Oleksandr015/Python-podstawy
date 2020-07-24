"""
DOOR CONTROLLER WITH LOCKING

Rozszerzmy działanie wcześniej stworzonej klasy DoorController. Chcemy, aby teraz klasa miała możliwość obsłużenia
zamknięcia drzwi na klucz.

Specyfikacja:
*   Rozszerzamy konstruktor o atrybut 'self._is_locked', który stanowi o tym czy drzwi są zablokowane. Jako początkową
    wartość przyjmuje False
*   Metoda 'lock()' zamyka i blokuje drzwi (wykonuje operacje close(), a potem dopiero blokuje drzwi). Blokowanie odbywa
    się poprzez odpowiednie ustawienie atrybutu 'self._is_locked'.
*   Metoda 'unlock()' odblokowuje drzwi, jednakże ich NIE OTWIERA (po odblokowaniu drzwi mają pozostać nadal zamknięte).
    Odblokowanie odbywa się poprzez odpowiednie ustawienie atrybutu 'self._is_locked'.
*   Metoda 'open()' zostaje rozszerzona. Oprócz wcześniejszego zachowania, czyli otwierania drzwi, zostaje do niej
    dodane sprawdzenie czy drzwi są zablokowane. Jeżeli drzwi są zablokowane, to zostaje rzucony wyjątek DoorLockedError
    z wiadomością 'The door is locked. Cannot open'. Jeżeli drzwi nie są zablokowane, to drzwi się otwierają.

**  Klasa wyjątku DoorLockedError została już zdefiniowana.
**  Wyjątek rzucamy za pomocą funkcji 'raise'. Polecam odwołać się do prezentacji!

W pliku test_door_controller napisz testy.

"""


class DoorLockedError(Exception):
    pass


class DoorController:

    def __init__(self):
        self._is_opened = False
        self._is_locked = False

    def is_door_opened(self):
        return self._is_opened

    def open(self):
        if self._is_locked:
            raise DoorLockedError('The door is locked. Cannot open')
        else:
            self._is_opened = True

    def close(self):
        self._is_opened = False

    def lock(self):
        self.close()
        self._is_locked = True
        return self._is_locked

    def unlock(self):
        self._is_locked = False
        return self._is_locked
