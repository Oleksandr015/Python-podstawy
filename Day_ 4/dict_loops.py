def print_phone_book(phone_book):
    for contact, numer in phone_book.items():
        print(f'{contact}:{numer}')


def student_with_at_list_points(student_points, points_limit):
    result = []
    for name, points in student_points.items():
        if points >= points_limit:
            result.append(name)
    return result

if __name__ == '__main__':
    phone_book = {'polise': 997, 'pizza': 476, 'emergency': 112}
    print(phone_book.keys())
    print(phone_book.values())
    print(phone_book.items())

    print_phone_book(phone_book)

    student_points = {'James': 12, 'Eva': 25, 'Peter': 19, 'Julius': 9}
    print(student_with_at_list_points(student_points, 20))
