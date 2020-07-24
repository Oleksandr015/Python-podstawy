class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def circuit(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'


if __name__ == '__main__':
    figure_1 = Rectangle(100, 50)
    print(figure_1)
    print(figure_1.width)
    print(figure_1.height)
    print(figure_1.area())
    print(figure_1.circuit())

    print('\n\n')

    figure_2 = figure_1
    figure_2.width = 700

    print(figure_2.width)
    print(figure_1.width)
    print(f'Figure 1: {figure_1}, {figure_2}')

    figure_1 = Rectangle(20, 20)
    print(f'Figure 1: {figure_1}, {figure_2}')

