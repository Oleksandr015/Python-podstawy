
class A:
    def __init__(self, a):
        self.a = a

    def square_value(self, value):
        return value ** 2

class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f'Hello! my name is {self.name}'


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def introduce(self):
        return f'{super().introduce()}. My color is {self.color}'


class Dog(Animal):
    def __init__(self, name, age, tail_length):
        super().__init__(name, age)
        self.tail_length = tail_length

    def introduce(self):
        return f'{super().introduce()}. My color is {self.tail_length}'


class Cow(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight


if __name__ == '__main__':
    burek = Dog('Burek', 2, 14)
    murka = Cat('Murka', 1, 'black')
    dzwon = Cow('Dzwon', 3, 200)

    a = A(5)
    b = B(12, 'Ala')
    print(b.a)
    print(b.b)
    print()
    print(a.square_value(5))
    print(b.square_value(5))
    print()

    print(burek.introduce())
    print(murka.introduce())
    print(dzwon.introduce())


#