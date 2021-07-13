def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=lambda x: sum([int(i) for i in x])))


if __name__ == '__main__':
    print(order_weight("103 123 4444 99 2000"))
