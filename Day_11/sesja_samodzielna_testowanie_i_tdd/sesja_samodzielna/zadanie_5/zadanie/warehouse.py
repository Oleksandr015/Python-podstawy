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
from Day_11.sesja_samodzielna_testowanie_i_tdd.sesja_samodzielna.zadanie_5.zadanie.product import Product


class Warehouse:
    def __init__(self, square_metres: float):
        self.square_metres = square_metres
        self.products_list = []

    def free_places_in_warehouse(self):
        sum_od_product = sum([pr.volume for pr in self.products_list])
        rest = self.square_metres - sum_od_product
        return rest

    def add(self, product: Product):
        rest = self.free_places_in_warehouse()
        if rest >= product.volume:
            self.products_list.append(product)
            return rest - product.volume
        else:
            return -1


