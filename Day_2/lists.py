if __name__ == '__main__':
    values = [1, 65, 6]
    print(values)

    print(values[1])
    print()
    products = ['milk', 'eggs', 'water']
    print(products)
    products[2] = 'onion'
    print(products)
    print()
    #Append to list
    values = [1, 5, 9]
    values.append(5)
    values.append(12)
    print(values)
    print()
    #Pop to list
    values.pop()
    print(values)
    values.pop(1)
    print(values)
    print()
    print(products[-1])
    print()
    print(len(products))
    print()
    values  = [1,2,3,4,5,7]
    print(values)
    values = [0] + values
    print(values)

    values = values[:-1] + [6] + values[-1:]
    print(values)