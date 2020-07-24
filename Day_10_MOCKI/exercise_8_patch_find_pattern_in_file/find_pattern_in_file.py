"""

FIND PATTERN IN FILE

Specyfikacja find_pattern_in_file:
*   do odczytu zawartosci pliku nalezy użyć funkcji read_file_lines(path) (z poprzedniego zadania)
*   funkcja zwraca True jeżeli w zwróconej liście stringów (zawartości pliku) znajduje się wzór podany przez parametr
    pattern. Zwraca False jeżeli wzór nie występuje w tym pliku.
    Np. lista ['abc', 'def'], pattern 'a' -> True;
    lista ['abc', 'def'], pattern 'z' -> False;
    lista ['byly sobie kurki trzy'], pattern 'kurki' -> True

Należy napisać testy tej funkcji w pliku test_find_pattern_in_file.py. Należy użyć konstrukcję
patch() aby zamockowac zewnetrzna funkcje read_file_lines(path).

"""
from Day_10_MOCKI.exercise_8_patch_find_pattern_in_file.file_reader import read_file_lines


def find_pattern_in_file(pattern: str, path: str) -> bool:
    list_result = read_file_lines(path)
    return pattern in ''.join(list_result)


    # for i in read_file_lines(path):
    #     if pattern in i:
    #         return True
    #     else:
    #         return False

if __name__ == '__main__':
    pattern = 'war'
    path = 'file'

    print(find_pattern_in_file(pattern, path))