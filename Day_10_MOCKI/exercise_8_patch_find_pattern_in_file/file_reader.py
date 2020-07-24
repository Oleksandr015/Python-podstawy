"""

FIND PATTERN IN FILE

Naszym celem jest stworzenie dwóch funkcji.
Pierwsza read_file_lines(path) znajdująca się w tym pliku, zwracająca listę
linijek z podanego pliku.
Druga find_pattern_in_file(pattern, path) sprawdza czy w pliku znajduje sie okreslony ciąg
znaków podany w parametrze pattern. Funkcja ta używa w sobie funkcji read_file_lines(path).

Specyfikacja read_file_lines:
*   otwiera podany plik w trybie 'r'
*   do wczytania wszystkich linijek należy użyć metody readlines() zwracającej listę linii pliku. Np. <plik>.readlines()
*   należy pamiętać o zamknięciu pliku po odczytaniu jego zawartości!

Na razie testy tej funkcji pominiemy.
"""


def read_file_lines(path):
    file = open(path, 'r')
    file_lines = file.readlines()
    file.close()
    return file_lines

#output
'''['It is a period of civil war.\n', 'Rebel spaceships, striking\n', 'from a hidden base, have won\n', 'their first victory against\n', 'the evil Galactic Empire.\n', '\n', 'During the battle, Rebel\n', 'spies managed to steal secret\n', "plans to the Empire's\n", 'ultimate weapon, the DEATH\n', 'STAR, an armored space\n', 'station with enough power to\n', 'destroy an entire planet.\n', '\n', "Pursued by the Empire's\n", 'sinister agents, Princess\n', 'Leia races home aboard her\n', 'starship, custodian of the\n', 'stolen plans that can save\n', 'her people and restore\n', 'freedom to the galaxy.....\n']'''


if __name__ == '__main__':
    path = 'file'
    print(read_file_lines(path))
