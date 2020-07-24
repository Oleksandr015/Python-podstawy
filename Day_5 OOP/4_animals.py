def dog_sound():
    return 'Hau!'


def cat_sound():
    return 'Miau!'


def cow_sound():
    return 'Mu!'


class Dog:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name}! Hau!'


class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name}! Miau!'


class Cow:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name}! Mu!'


if __name__ == '__main__':
    burek = Dog('Burek')
    murka = Cat('Murka')
    dzwon = Cow('Dzwon')

    print(dog_sound())
    print(cat_sound())
    print(cow_sound())

    print(burek.sound())
    print(murka.sound())
    print(dzwon.sound())

    #animals = [burek, murka, dzwon]
#
    #for animal in animals:
    #    print(animal.sound())