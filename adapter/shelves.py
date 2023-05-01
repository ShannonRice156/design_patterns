"""A module to which holds all shelf functionality"""
from typing import Protocol


class shelf(Protocol):
    """An interface for a shelf"""

    def restock(self) -> None:
        pass


class FruitShelf():
    """A Fruit shelf """

    def restock(self) -> None:
        """Restocks this shelf"""
        print("restocking the fruit shelf")


class ChocShelf():
    """A Chocolate shelf """

    def restock(self) -> None:
        """Restocks this shelf"""
        print("restocking the Choc shelf")
