def print_values(values):
    for i in values:
        print(i)


def print_values_2(values):
    for index in range(len(values)):
        print(values[index])


def sum_values(values):
    result = 0
    for value in values:
        result += value

    return result


def min_values(values):
    result = 0
    for value in values:
        if values[value] < result:
            result = values[value]
    return result


def square_values(values):
    result = []
    for i in values:
        result.append(i ** 2)
    return result

def get_even_values(values):
    result = []
    for i in values:
        if i % 2 == 0:
            result.append(i)
    return result



if __name__ == '__main__':
    print(list(range(5)))
    print(len(range(5)))

    print_values([0, 1, 2, 3, 4])
    print()

    print(min_values([0, 1, 2, 3, 4]))
    print()

    print(square_values([0, 1, 2]))

    print()

    print(get_even_values([0, 1, 2]))
