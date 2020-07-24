if __name__ == '__main__':
    values = {1, 2, 3, 4}
    print(values)

    values_2 = {3, 3, 3, 3, 4, 4, 5}
    print(values_2)

    list_with_duplicates = {1, 2, 2, 3, 3, 5}
    print(list(set(list_with_duplicates)))

    # print(values[0]) not possible

    for value in values:
        print(value)

    for i, value in enumerate(values):
        print(f'{i}:{value}')

    print()
    first_set = {1, 2, 3, 4, 5}
    second_set = {4, 5, 6, 7, 8}

    print(first_set | second_set)
    print(first_set & second_set)
    print(first_set - second_set)
    print(second_set - first_set)
    print(first_set ^ second_set)
    print()

    numbers = set()
    numbers.add(5)
    numbers.add(5)
    print()

    numbers.update({5, 1, 2, 3})
    print(numbers)
    print(len(numbers))
    print(max(numbers))
    print(min((numbers)))
    print(sum(numbers))
    print()

    numbers = {1,2,3,4}
    print(5 in numbers)
    print(2 in numbers)
    print(numbers.issubset({1,2,3,4,5}))
    print(numbers.issubset({1,2}))
    print(numbers.issuperset({1,2,3,4,5}))
    print(numbers.issuperset({1,2}))
