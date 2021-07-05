def pig_it(text):

    new_t = text.split()
    create_t = []
    punc = []

    for word in new_t:
        if word in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            punc.append(word)
        elif word.isalpha():
            create_t.append(word[1::] + word[0] + 'ay')

    return ' '.join(create_t + punc)


if __name__ == '__main__':
    print(pig_it('Pig latin is cool !')) # 'igPay atinlay siay oolcay !')
    print(pig_it('This is my string')) # 'hisTay siay ymay tringsay')