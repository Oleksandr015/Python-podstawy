from abc import ABC, abstractmethod
from typing import Tuple, List, Dict


class Instrument(ABC):
    def __init__(self, weight: float):
        self.weight = weight


    @abstractmethod
    def play(self):
        pass


class Guitar(Instrument):
    def __init__(self, weight: float, strings: int):
        super().__init__(weight)
        self.strings = strings

    def play(self):
        return 'Guitar plays'

class Flute(Instrument):
    pass

class Violin(Instrument):
    pass

def play_instrument(instrument: List[Instrument]):
    pass


if __name__ == '__main__':
    #instrument = Instrument(1.3)
    guitar = Guitar(1.5, 6)
    instrument: List[Instrument] = [guitar]