"""A module to show an example of the Builder design pattern"""

from enum import Enum
from dataclasses import dataclass
from misc.colours import Colours


class DoorShape(Enum):
    """Enumeration for door shapes"""

    circle = 0
    square = 1
    arch = 2


@dataclass(frozen=True)
class Window:
    """A class which holds all window data"""
    colour: Colours = Colours.red
    width: int = 0
    height: int = 0
    cost: int = 0


@dataclass(frozen=True)
class Bricks:
    """A class which holds all brick data"""
    colour: Colours = Colours.red
    cost: int = 0
    quantity: int = 0

    def total_cost(self):
        """Returns the total cost of the bricks based on the quantity and cost per brick"""
        return self.quantity * self.cost


@dataclass(frozen=True)
class Door:
    """A class which holds all door data"""

    colour: Colours = Colours.red
    width: int = 0
    height: int = 0
    cost: int = 0
    shape: DoorShape = DoorShape.circle


class Mansion():
    """A class to represent the functionality for a building a mansion"""

    def set_window(self, window: Window) -> None:
        """Set this objects instance of window to the parameter given"""
        self._window = window

    def set_bricks(self, bricks: Bricks) -> None:
        """Set this objects instance of bricks to the parameter given"""

        self._window = bricks

    def set_door(self, door: Door) -> None:
        """Set this objects instance of door to the parameter given"""

        self._door = door


def main():
    '''Main method which will execute the builder pattern example'''

    m = Mansion()
    win = Window(width=100, height=100, colour=150)
    m.set_window(win)

    b = Bricks(quantity=100, colour=Colours.green, cost=50)
    m.set_bricks(b)

    d = Door(colour=Colours.green, width=80, height=80, shape=DoorShape.arch)
    m.set_door(d)
