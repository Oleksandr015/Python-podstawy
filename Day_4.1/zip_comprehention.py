def add_respective_values(first_list, second_list):
    result = []
    for value_1, value_2 in zip(first_list, second_list):
        result.append(value_1 + value_2)
    return result

def add_respective_values_lc(first_list, second_list):
    return [value_1 + value_2 for value_1, value_2 in zip(first_list, second_list)]

def sum_lists_even(list_in_list):
    result = []
    for list in list_in_list:
        if len(list) % 2 == 1 and list[0] > 1:
            result.append(sum(list))
    return result

def sum_lists_even_zc(list_in_list):
    return [sum(list) for list in list_in_list if len(list) %2 == 1 and list[0]]


#def filter_students(students, points, leght):
#    return [name[::-1] for name, points_students in student]



if __name__ == '__main__':
    first_list = [4,5,1,2]
    second_list = [0,-5,-1,0]
    print(add_respective_values(first_list, second_list))
    print(add_respective_values_lc(first_list, second_list))

    list_in_list = [[11], [1,0,1], [2,2,2,2], [5,1,5]]
    print(sum_lists_even(list_in_list))

    print(sum_lists_even_zc(list_in_list))
    print()

    values = [('James', 9), ('Eva', 10), ('Piotr', 8), ('Anna', 4)]
    #print(filter_students(values, 7, 3))