def double_name_and_age(name, age):
    name = name + name
    age = age * 2
    return name, age

if __name__ == '__main__':
    numbers = (1,2,3,4)
    print(numbers)
    print(numbers[3])
    print(numbers[-1])

    crazy_tuple = (True, 'Eva', 3, 4.5)
    print(crazy_tuple)
    print()

    #crazy_tuple[0] = False - niemodyfikowalna
    #crazy_tuple.append(4)

    print(len(numbers))
    print(max(numbers))
    print(min(numbers))
    print()


    for value in numbers:
        print(value)

    texts = ('Eva', 'James')
    name_1, name_2 = texts
    print(name_1)
    print(name_2)
    print()

    print((1,2,3) == (1,2,3))
    print((1,2,3) == (1,2,3,4))
    print()

    print(double_name_and_age('Eva', 25))
    name, age = double_name_and_age('Eva', 25)
    print(f'{name}, {age}')

