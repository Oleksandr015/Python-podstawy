def order_weight(strng):
    strng = strng.split()
    #result = sorted(strng, key lambda x: [sum(i) for i in strng])
    weight_dict = {}
    for w in strng:
        weight_dict[w] = sum(int(x) for x in w)
        a = sorted(weight_dict.items(), key=lambda x: x[1])
        b=[x[0] for x in a]

    return a

if __name__ == '__main__':
    print(order_weight("103 123 4444 99 2000"))