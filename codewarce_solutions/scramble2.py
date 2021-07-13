from collections import Counter


def scramble(s1, s2):

    dict1 = Counter(s1)
    dict2 = Counter(s2)

    commonDict = dict1 & dict2
    return len(list(commonDict.elements())) == len(s2)


if __name__ == '__main__':
    print(scramble('scriptjava', 'javascript'))
