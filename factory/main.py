"""A module to show an example of the factory design pattern"""

from abc import ABC, abstractmethod


class Fruit(ABC):
    """Abstract base class for a piece of fruit"""

    def __init__(self) -> None:
        self._slice_fruit()

    def _slice_fruit(self) -> None:
        """Assigns variable returned by slice method to slice variable"""
        self.slice = self.slice()

    def get_slice_type(self) -> str:
        """Returns slice type"""
        return self.slice.slice_type()

    @abstractmethod
    def slice(self):
        ...


class Slice(ABC):
    """Abstract base class for a slice object"""
    @abstractmethod
    def slice_type(self) -> str:
        ...


class AppleSlice(Slice):
    """A class which represents a Apple slice"""

    def slice_type(self) -> str:
        return "Apple"


class PearSlice(Slice):
    """A class which represents a Pear slice"""

    def slice_type(self) -> str:
        return "Pear"


class Pear(Fruit):
    """A class which represents a Pear"""

    def slice(self) -> PearSlice:
        return PearSlice()


class Apple(Fruit):
    """A class which represents an Apple"""

    def slice(self) -> AppleSlice:
        return AppleSlice()


def main():
    """The main function which executes the factory design pattern"""

    fruit1 = Apple()
    fruit2 = Pear()

    print(f"Slice of {fruit1.get_slice_type()}")
    print(f"Slice of {fruit2.get_slice_type()}")
