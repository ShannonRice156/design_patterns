"""A module to show an example of the iterator design pattern"""

from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class Item:
    name: str
    price: int
    quantity: int

    def total_price(self) -> int:
        return self.price * self.quantity


@dataclass(frozen=True)
class Item2(Item):
    name2: str
    price2: int
    quantity2: int


@dataclass
class MarketItems:
    """A iterator that holds all market item data """
    arr: list
    index: int = -1

    def __init__(self, path: str) -> None:
        self.arr = []
        with open(path) as f:
            lines = f.readlines()
            for line in lines:
                split = line.removesuffix("\n").split(",")
                new_item = Item(split[0], int(split[1]), int(split[2]))
                self.arr.append(new_item)

    def __iter__(self) -> Self:
        """Returns the iterator object"""
        self.index = -1
        return self

    def __next__(self) -> Item:
        """Returns the next item"""

        if (self.index + 1) >= len(self.arr):
            raise StopIteration
        else:
            self.index += 1
            return self.arr[self.index]


def print_array(items: MarketItems) -> None:
    """Iterates through items and prints each item"""
    for item in items:
        print(item)


def main() -> None:
    """The main function which executes the iterator"""

    items = MarketItems("marketitems.txt")
    new_item = Item2("djdj", 5, 5, "dfhfh", 6, 6)
    print_array(items)
    print_array(items)
    print(new_item)
