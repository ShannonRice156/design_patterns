"""A module to show an example of the flyweight design pattern"""

from dataclasses import dataclass
from enum import Enum


class ShelfType(Enum):
    """Enumeration for shelf type"""

    Choc = 1
    Fruit = 2
    Dairy = 3
    Bread = 4


@dataclass(frozen=True)
class StoreItem:
    """A class which holds all data associated with a store item"""

    name: str
    cost: float


class Shelf:
    """Class that represents a shelf and all its contents"""

    def __init__(self) -> None:
        self.items = {}
        self._stock = {}

    def stock(self, name: str, cost: float, num: int) -> None:
        """Function to stock shelf with new storeitems based on parameters given"""
        item = StoreItem(name, cost)
        self.items[name] = item
        self.order(name, num)

    def order(self, name: str, num: int) -> None:
        """Order new items based on the name and number of items given in parameters"""
        self._stock.setdefault(name, 0)
        self._stock[name] += num

    def inventory_num(self):
        """Returns number of this item the shelf has in stock"""
        return sum(self._stock.values())

    def total_profit(self):
        """Returns the total profit to be made by the items in stock"""
        for name, num in self._stock.items():
            profit += self.items[name].cost * num
        return profit


class Store:
    """Class that represents a store and all its shelves"""

    def __init__(self) -> None:
        self.shelves = []
        self.num = {}
        self.max_shelf = 3

    def add_shelf(self, shelf: Shelf, shelf_type: ShelfType) -> None:
        """Adds new shelf of type given if store does not already have maximum amount of shelves"""
        self.num.setdefault(shelf_type, 0)
        if self.num[shelf_type] == self.max_shelf:
            print(f"Max number of {shelf_type.name} shelves added")
        else:
            self.shelves.append(shelf)
            self.num[shelf_type] += 1

    def inventory_num(self) -> int:
        """Accumulates all shelves and their inventories and returns total number"""
        num = 0
        for shelf in self.shelves:
            num += shelf.inventory_num()
        return num

    def total_profit(self):
        """Accumulates all profit to be made from current inventory and returns the total"""

        for shelf in self.shelves:
            profit += shelf.total_profit
        return profit


def main() -> None:
    """The main function which executes the flyweight design pattern"""

    store = Store()
    shelf = Shelf()
    shelf.stock("Cheese", 10, 100)
    shelf.stock("Milk", 15, 80)
    store.add_shelf(shelf, ShelfType.Dairy)
    print(f"Total inventory for all shelves is {store.inventory_num()}")
