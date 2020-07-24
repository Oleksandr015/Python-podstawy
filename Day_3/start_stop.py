def even_square(start, stop):
    lista_even = []
    for i in range(start, stop + 1):
        if i % 2 == 0:
            lista_even.append(i**2)
        return lista_even[1:]



if __name__ == '__main__':
    start = int(input())
    stop = int(input())
    print(even_square(start, stop))
