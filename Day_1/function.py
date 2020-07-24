#def add_two_number(number_1, number_2):
#    result = number_1 + number_2
#    return result
#
#
#if __name__ == '__main__':
#    value = add_two_number(5, 4)
#    print(value)
#
#
#def multipl_three_number(number_1, number_2, number_3 ):
#    result = number_1 * number_2 * number_3
#    return result
#

#if __name__ == '__main__':
#    value1 = multipl_three_number(5, 4, 3)
#    print(value1)

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_even(7))