def scramble(s1, s2):
    for i in s2:
        if i not in s1:
            return False
        else:
            s2.replace(i, '')
    return True


if __name__ == '__main__':
    print(scramble('rkqodlw', 'world'))
