def list_difference(list_1, list_2):
    result = 0
    for index in range(len(list_1)):
        if list_1[index] != list_2[index]:
            result += 1
    return result

def list_difference_zip(list_1, list_2):
    result = 0
    for value_1,value_2 in zip(list_1, list_2):
        if value_1 != value_2:
            result +=1
    return result


if __name__ == '__main__':
    shopping_items = ['eggs', 'ham', 'cheese']
    quantities = [4, 2, 6]

    print(list(zip(shopping_items, quantities)))

    colors = ['red', 'green', 'blue']
    names = ['James', 'Anna', 'Donald', 'Eva']
    print(list(zip(colors, names)))
    # sprawdzic kod!

    list_1 = [1, 2, 3, 4]
    list_2 = [1, 2, 3, 4, 5, 6]
    list_3 = [1, 2, 3, 4]

    print(list(zip(list_1, list_2, list_3)))
    print(list_difference([1, 2, 3, 4], [0, 2, 3, 5]))


    print(list_difference_zip([1, 2, 3, 4], [0, 2, 3, 5]))