if __name__ == '__main__':
    phone_book = {'polise': 997, 'pizza': 476, 'emergency': 112}
    print(phone_book)
    print(phone_book['polise'])

    phone_book['girlfriend'] = 'Forever alone :P'
    print(phone_book)
    phone_book['pizza'] = 568
    print(phone_book)
    del phone_book['girlfriend']
    print(phone_book)

    phone_book[361] = 'Restaraunt'
    print(phone_book)

    print()
    print(phone_book)
    print(phone_book.get('James'), 'invalid contact')
