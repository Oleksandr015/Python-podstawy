def build_dict_from_lists(keys, values):
    return {key: value for key, value in zip(keys, values)}


def reverse_dict(dictionary):
    return {value: key for key, value in dictionary.items()}


def square_even_phones(phone_book):
    return {key: value ** 2 for key, value in phone_book.items() if value % 2 == 0}


variable = 12
if type(variable) is int:
    print('Variable is int')

if type(variable) == int:
    print('Variable is int')

variable = 'Eva'
if type(variable) == str:
    print('Variables is str')


if __name__ == '__main__':
    names = ['James', 'Eva', 'Piotr']
    phone = [453, 764, 124]

    print(build_dict_from_lists(names, phone))
    phones_book = build_dict_from_lists(names, phone)
    print(reverse_dict(phones_book))

    print(square_even_phones(phones_book))
