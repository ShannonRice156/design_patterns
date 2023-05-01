"""A module to show an example of the command design pattern"""

from typing import Protocol
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Vector():
    """Dataclass which holds all information for a vector"""
    x: float
    y: float


class MovementItem(Protocol):
    """Interface representing an item that can moved"""

    def __init__(self, position: Vector) -> None:
        ...

    def move(self, amount: Vector):
        ...


class ChessPiece():
    """A class representing a Chess piece"""

    def __init__(self, position: Vector) -> None:
        self.position = position

    def move(self, amount: Vector):
        """Move the Chess piece by the amount given and output the resulting movement """
        original = deepcopy(self.position)
        self.position.x += amount.x
        self.position.y += amount.y
        print(
            f'Moved ChessPiece from {original.x},{original.y} to {self.position.x},{self.position.y}')


class Cheeter():
    """Class representing a Cheeter"""

    def __init__(self, position: Vector) -> None:
        self.position = position

    def move(self, amount: Vector):
        """Move the position by the amount given in the parameters and output the coordinates of the movement"""
        original = deepcopy(self.position)
        self.position.x += (amount.x * 2)
        self.position.y += (amount.y * 2)
        print(
            f'Moved Cheeter from {original.x},{original.y} to {self.position.x},{self.position.y}')


class Movement(Protocol):
    """Interface representing movement that can be made"""

    def move(self, movementitem: MovementItem, amount: Vector) -> None:
        ...


class Walker():
    """A class representing someone that is walker"""

    def move(self, movementitem: MovementItem, amount: Vector) -> None:
        """Use the movementitem and vector given in the parameters to walk"""
        print("Walking........")
        movementitem.move(amount)


class Runner():
    """A class representing someone that is a runner"""

    def move(self, movementitem: MovementItem, amount: Vector) -> None:
        """Use the movementitem and vector given in the parameters to run"""

        print("Running........")
        movementitem.move(amount)


class Mover():
    """A class representing a mover that invokes movement for a given movement item and vector amount."""

    def invoke(self, move: Movement, movementitem: MovementItem, amount: Vector) -> None:
        """Invokes the given move object's move method with the given movement item and vector amount as parameters"""
        move.move(movementitem, amount)


def main() -> None:
    '''Main method which will execute the command pattern example'''

    mover = Mover()
    print("Chess Piece")
    mover.invoke(Walker(), ChessPiece(Vector(x=3, y=5)), Vector(x=3, y=4))

    print("Cheeter")
    mover.invoke(Runner(), Cheeter(Vector(x=3, y=5)), Vector(x=5, y=5))
