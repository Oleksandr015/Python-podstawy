from typing import List

class Sensor:
    def __init__(self, location: str):
        self.location: str = location
        self.measurement: float = 0
        self.precision: float = float('inf')
        self.unit: str = 'N/A'
        self.log: List[float] = []

    @property
    def log_average(self):
        return sum(self.log) / len(self.log)

    def update(self, measurement: float):
        self.measurement = measurement
        self.log.append(self.measurement)

    @property
    def description(self):
        return f'{self.measurement} +/- {self.precision} [{self.unit})]'

    def __len__(self):
        return len(self.log)

class Thermometer(Sensor):
    def __init__(self, location):
        super().__init__(location)
        self.unit: str = 'C'
        self.precision: float = float('inf')

    @property
    def fahrenheit(self):
        return f'{self.measurement * 1.8 + 32} +/- {self.precision} [F]'

class PressureSensor(Sensor):
    def __init__(self, location):
        super().__init__(location)
        self.unit: str = 'hPa'
        self.precision: float = float('inf')


    @property
    def bar(self):
        return f'{self.measurement/1000} +/- {self.precision} [bar]'



if __name__ == '__main__':
    sensor = Sensor("Dom")
    print(sensor.log)
    sensor.update(5)
    sensor.update(10)
    print(sensor.log_average)
    sensor = Thermometer("Dom")
    print(sensor.update(12.5))
    print(len(sensor))
    print(sensor.description)
    print(sensor.fahrenheit)

    barometr = PressureSensor('Garden')
    barometr.update(1015)
    barometr.update(1024)
    print(barometr.precision)
    print(barometr.bar)




'''Wszędzie stosujemy Type Hinting!!!
Stwórz klasę Sensor, która będzie klasą nadrzędną dla kolejnych klas.
Niech metoda __init__ definiuje następujące atrybuty:
Metoda ta powinna przyjmować jeden argument location (określający położenie czujnika - np. 'dom') i zapisywać go jako atrybut obiektu, a dodatkowo tworzyć"
measurement (wielkość zmierzona przez czujnik - domyślnie 0),
precision (niedokładność pomiaru - domyślnie przyjmuje wartość float('inf'), co jest równoważne nieskończoności), 
unit( jednostka, domyślnie 'N/A').
Dodaj jako atrybut pustą listę log, która docelowo ma przechowywać historię pomiarów.
Zdefiniuj property log_average, zwracające średnią wartość pomiarów wykonanych przez czujnik.
W celu aktualizowania wartości pomiaru utwórz funkcję update, króra przyjmuje wartość pomiaru, przypisuje ją do zmiennej measurement, oraz doda ją również do listy pomiarów historycznych log
Zdefiniuj property description, które zwracać będzie łańcuch znaków w następującej postaci: 'pomiar +/- dokładność [jednostka]'
2. Stwórz klasę Thermometer, dziedziczącą po klasie Sensor.
• Metoda __init__, oprócz pobierania lokalizacji czujnika, powinna ustawiać jednostkę czujnika unit  na stopnie ('C') oraz dokładność pomiaru precision.
• Jeśli uznasz, że konieczne jest zaimplementowanie dodatkowych metod (np. przykrycie metod zdefiniowanych w klasie Sensor) - zrób to.
• Zdefiniuj property fahrenheit, które zwróci opis aktualnej wartości pomiaru w stopniach Fahrenheita
3. Stwórz klasę PressureSensor, dziedziczącą po klasie Sensor.
• Metoda __init__ - analogicznie jak dla termometru (domyślna jednostka - 'hPa').
• Jeśli uznasz, że konieczne jest zaimplementowanie dodatkowych metod (np. przykrycie metod zdefiniowanych w klasie Sensor) - zrób to.
• Zdefiniuj property bar, które zwróci opis aktualnej wartości pomiaru w barach
4. Utwórz po dwa czujniki z każdej klasy (zlokalizowane np. w domu i na dworze) i "pobaw" się poszczególnymi metodami. :slightly_smiling_face: (edited) (edited) '''