def createFib(n):
    if n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return createFib(n - 1) + createFib(n - 2)


def productFib(prod):
    position = 1
    b = []
    a = 0
    while a < prod:
        a = createFib(position) * createFib(position + 1)

        if a == prod:
            return [createFib(position), createFib(position+1), True]
        position += 1
        if a > prod:
            return [createFib(position-1), createFib(position), False]



if __name__ == '__main__':
    print(productFib(5895))
