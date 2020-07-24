def get_even_lenght_words(words):
    result = []
    for word in words:
        if len(word) % 2 == 0:
            result.append(word)
    return result


def cut_even_length_words(text):
    result = []
    for word in text.split(' '):
         if len(word) %2 ==1:
             result.append(word)

    return result




if __name__ == '__main__':
    #name = "James"
    #print(name[0])
    #print(name[-1])
    #print(list(name))
    #print(len(name))
    #print('ala ma kota'.count('a'))
    #print(name[::-1])
#
    #print(get_even_lenght_words(['lal', 'beer', 'm', 'piotr', 's']))
#
    #print('ala ma kota'.split(' '))
    #print('-*-'.join(['ala', 'ma', 'kota']))

    print(cut_even_length_words("aaa bb c bb aaaa"))