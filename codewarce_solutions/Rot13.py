import string


def rot13(message):
    alphabet_low = string.ascii_lowercase * 2
    alphabet_up = string.ascii_uppercase * 2

    res = []
    for lett in message:
        if lett not in string.ascii_letters:
            res.append(lett)
        elif lett.islower():
            res.append(alphabet_low[alphabet_low.find(lett) + 13])
        else:
            res.append(alphabet_up[alphabet_up.find(lett) + 13])
    return ''.join(res)


if __name__ == '__main__':
    print(rot13("Test"))  # grfg
