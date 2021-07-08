def sum_pairs(ints, s):
    seen=[]
    for item in ints:
        if s-item in seen: return [s-item, item]
        if item not in seen: seen+=[item]
    return None



if __name__ == '__main__':
    l4 = [1, 2, 3, 4, 1, 0]

    print(sum_pairs(l4, 2))
