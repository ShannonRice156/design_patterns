"""A module to show an example of the adapter design pattern"""

from .shelves import FruitShelf, ChocShelf, shelf


class ShelfHolder():
    """A class representing a holder for a collection of shelves."""

    def __init__(self, shelves: list[shelf]):
        """Initializes a new ShelfHolder object with the given list of Shelf objects."""
        self.shelves = shelves

    def restock_all(self):
        """Restocks all shelves within this object"""
        for shelf in self.shelves:
            shelf.restock()


def main() -> None:
    '''Main method which will execute the adapter example code'''

    shelves = [FruitShelf(), ChocShelf()]
    s = ShelfHolder(shelves)
    s.restock_all()
