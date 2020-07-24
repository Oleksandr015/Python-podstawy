def copy_list(values):
    result = []
    for value in values:
        result.append(value)

    return result


def copy_list_lc(values):
    return [value for value in values]


def square_list(values):
    result = []
    for value in values:
        result.append(value ** 2)
    return result


def square_list_lc(values):
    return [value ** 2 for value in values]


def square_even_values(values):
    result = []
    for value in values:
        if value % 2 == 0:
            result.append(value**2)
    return result


def square_even_values_lc(values):
    return [value**2 for value in values if value % 2 == 0]

def sum_points(values):
    return sum([value[1] for value in values])

def longest_name_lenght(values):
    return max([len(value[0]) for value in values])

def zip_function(a,d):
    return zip(a,d)


def print(param):
    pass


if __name__ == '__main__':
    print(copy_list([3, 4, 5, 6]))
    print(copy_list_lc([2, 4, 5, 7]))

    print(square_list([2, 7, 1, 3]))
    print(square_list_lc([2, 7, 1, 3]))
    print()
    print(square_even_values([3, 4, 5, 6]))
    print(square_even_values_lc([3, 4, 5, 6]))

    values = [('James', 9), ('Eva', 10), ('Piotr', 8), ('Anna', 4)]
    print(sum_points(values))
    print(longest_name_lenght(values))


    a = (1,2,3)
    d = (5,6,7)

    print(zip_function(a,d))
