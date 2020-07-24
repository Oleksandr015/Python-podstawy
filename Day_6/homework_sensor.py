from abc import ABC
from typing import List

class Sensor:
    def __init__(self, location: str):
        self.location:str = location
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

    def description(self):
        return f'{self.measurement} +/- {self.precision} [{self.unit}]'

class Thermometer(Sensor):
    def __init__(self, location: str):
        super().__init__(location)
        self.unit: str = 'C'
        self.precision:float = 0.1

    def fahrenheit(self):
        return f'{self.measurement * 9/5 + 32} +/- {self.precision} [F]'

class PressureSensor(Sensor):
    def __init__(self, location: str):
        super().__init__(location)
        self.unit: str = 'hPa'
        self.precision: float = 3

    @property
    def bar(self):
        return f'{self.measurement / 1000} +/- {self.precision} [bar]'













if __name__ == '__main__':
    sensor_1 = Sensor('Dom')
    sensor_1.update(5)
    sensor_1.update(9)
    print(sensor_1.log)
    print(sensor_1.log_average)
    print(sensor_1.description)
    thermometr_1 = Thermometer('Inside house')
    print(thermometr_1.fahrenheit)
    pressure = PressureSensor('Mountains')
    pressure.update(1015)
    pressure.update(1024)
    print(pressure.description)
    print(pressure.bar)
