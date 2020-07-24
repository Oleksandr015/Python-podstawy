"""
ZADANIE 5

Napisz klasę, która będzie reprezentowała magazyn. Pojemność magazynu (wartość float odzwierciedlająca metry
sześcienne) jest definiowana przez konstruktor. Stwórz klasę, która będzie odzwierciedlać produkt. Objętość produktu
jest definiowana przez konstruktor. Magazyn będzie miał metodę "add", która będzie przyjmować za argument obiekt
typu Product i zwracać pozostałą ilość wolnej przestrzeni lub -1 jeśli nie można dodać nowej rzeczy, bo już się nie
zmieści w magazynie.

Użyj fixtur (setUp) by przygotować zestaw produktów, które co miesiąc wpływają do magazynów i stwórz testy, które sprawdzą,
czy magazyny poprawnie reagują na dodawanie do nich kolejnych produktów. Dokładność do dwóch miejsc po przecinku.

** dla chetnych zamiast zestawów produktór typu Product użyć MagicMock, zachecam goraco do zmierzenia się

"""
from sesja_samodzielna.zadanie_5.rozwiazanie.product import Product


class Warehouse:
    def __init__(self, capacity: float):
        self.capacity = capacity
        self.products = []

    def __calculate_free_space(self):
        sum_od_products = sum([x.volume for x in self.products])
        return self.capacity - sum_od_products

    def add(self, product: Product):
        rest_space = self.__calculate_free_space()
        if rest_space >= product.volume:
            self.products.append(product)
            return rest_space - product.volume
        else:
            return -1
