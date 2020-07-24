from typing import List


class Sensor:
    def __init__(self, location: str):
        self.location: str = location
        self.measurement: float = 0
        self.precision: float = float('inf')
        self.unit: str = 'N/A'
        self.log: List[float] = []

    def update(self, measurement: float):
        self.measurement = measurement
        self.log.append(measurement)

    @property
    def log_average(self):
        return sum(self.log) / len(self.log)

    @property
    def description(self):
        return f'{self.measurement} +/- {self.precision} [{self.unit}]'

    def __len__(self):
        return len(self.log)


class Thermometer(Sensor):
    def __init__(self, location: str):
        super().__init__(location)
        self.precision = 0.1
        self.unit = 'C'

    @property
    def fahrenheit(self):
        return f'{self.measurement * 1.8 + 32} +/- {self.precision} [F]'


class PressureSensor(Sensor):
    def __init__(self, location):
        super().__init__(location)
        self.precision = 5
        self.unit = 'hPa'

    @property
    def bar(self):
        return f'{self.measurement / 1000} +/- {self.precision} [bar]'


if __name__ == '__main__':
    sensor = Thermometer('Dom')
    print(sensor.log)
    sensor.update(5)
    sensor.update(10)
    print(sensor.log_average)
    print(len(sensor))
    print(sensor.description)
    print(sensor.fahrenheit)

    barometr = PressureSensor('Garden')
    barometr.update(1015)
    barometr.update(1024)
    print(barometr.description)
    print(barometr.bar)