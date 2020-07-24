#wejście : 'zielono-czerwono-czarno-biały'
#wynik: 'biało-czarno-czerwono-zielono'

def sort_srting(long_string):
    new_srting = long_string.split('-')
    new_srting.sort()
    return "-".join(new_srting)


def return_count_items_more_5symbols(list_characters):
    result = 0
    for char in list_characters:
        if len(str(char)) >= 5 and char[0] == char[-1]:
            result += 1
    return result

'''Napisz funkcję, która przyjmuje listę liczb całkowitych i zamienia ją na jedną liczbę całkowitą.
Wejście: [11, 33, 5, 0]
Oczekiwane wyjście: 113350'''

def concatenations_intengers(list_of_intengers):


    return ''.join(map(str, list_of_intengers))






if __name__ == '__main__':
    long_string = 'zielono-czerwono-czarno-biały'
    print(sort_srting(long_string))

    print()


    list_characters = ['beereeb', 'car', 55, True, 'solarys']
    print(return_count_items_more_5symbols(list_characters))

    print()

    list_of_intengers = [11, 33, 5, 0]
    print(concatenations_intengers(list_of_intengers))
