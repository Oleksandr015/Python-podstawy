def get_perfect_students_indexes(first_list, second_list):
    result = []
    for index in range(len(first_list)):
        if first_list[index] and second_list[index]:
            result.append(index)
    return result


def get_perfect_students_indexes_2(first_list, second_list):
    result = []
    for index, (first_value, second_value) in enumerate(zip(first_list, second_list)):
        if first_value and second_value:
            print(f'index: {index}, value: {first_value}')
            result.append(index)
    return result


def get_indexes_and_products_more_than_five(products, quantities):
    result = []
    for index, (product, quantity) in enumerate(zip(products, quantities)):
        if quantity > 5:
            print(f'{index}, {product}: {quantity}')
            result.append((index, product))
    return result


if __name__ == '__main__':
    names = ['Eva', 'Piotr', 'James']

    first_attendance_list = [True, True, False, False, True]
    second_attendane_list = [True, True, False, True, False]

    print(get_perfect_students_indexes_2(first_attendance_list, second_attendane_list))
    products = ['eggs', 'apples', 'bananas', 'milk']
    quantities = [4,7,2,12]
    print(get_indexes_and_products_more_than_five(products, quantities))