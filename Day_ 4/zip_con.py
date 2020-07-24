def sum_lists_even(list_in_list):
    result = []
    for list in list_in_list:
        if len(list) % 2 == 1 and list[0] > 1:
            result.append(sum(list))

    return result


def sum_lists_even_zc(list_in_list):
    return [sum(list) for list in list_in_list if len(list) % 2 == 1 and list[0]]


if __name__ == '__main__':

    list_in_list = [[11], [1, 0, 1], [2, 2, 2, 2], [5, 1, 5]]
    print(sum_lists_even(list_in_list))

    print(sum_lists_even_zc(list_in_list))
