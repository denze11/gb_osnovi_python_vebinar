from abc import ABC, abstractmethod

from typing import Any


class AbstractTextil(ABC):
    @property
    @abstractmethod
    def required_fabric(self):
        pass

    @property
    @abstractmethod
    def dimension(self):
        pass

    @abstractmethod
    def _calc_required_fabric(self):
        pass


class Textil(AbstractTextil):
    _textil = []

    def __init__(self, name: str, dimension: Any):
        self.name = name
        self._dimension = dimension
        self._required_fabric = None

        self._textil.append(self)

    def _calc_required_fabric(self):
        raise NotImplemented

    @property
    def required_fabric(self) -> float:
        if not self._required_fabric:
            self._calc_required_fabric()

        return self._required_fabric

    @property
    def dimension(self) -> Any:
        return self._dimension

    @dimension.setter
    def dimension(self, dimension: Any):
        self._dimension = dimension
        self._required_fabric = None

    @property
    def total_required_fabric(self):
        return sum([item.required_fabric for item in self._textil])


class Coat(Textil):
    def _calc_required_fabric(self):
        self._required_fabric = round(self.dimension / 6.5 + 0.5, 2)

    @property
    def V(self) -> Any:
        return self.dimension

    @V.setter
    def V(self, size: Any):
        self.dimension = size

    def __str__(self):
        return f"Для пальто {self.dimension} размера " \
               f"необходимо {self.required_fabric} кв. метров ткани"


class Suit(Textil):
    def _calc_required_fabric(self):
        self._required_fabric = round(2 * self.dimension * 0.01 + 0.3, 2)

    @property
    def H(self) -> Any:
        return self.dimension

    @H.setter
    def H(self, height: Any):
        self.dimension = height

    def __str__(self):
        return f"Для костюма на рост {self.dimension} см. " \
               f"необходимо {self.required_fabric} кв. метров ткани"


coat = Coat('Пальто от Chanel', 7)
print(coat)
coat.V = 8
print(coat)

suit = Suit('Костюм от Stuart Hughes', 173)
print(suit)
suit.H = 180
print(suit)

print(coat.total_required_fabric)
print(suit.total_required_fabric)
