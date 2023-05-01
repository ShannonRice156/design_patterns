"""A module which holds all data and classes associated with a house"""
from .tools import Tools


class House():
    """A class which represents a house and its properties"""

    def __init__(self) -> None:
        self._width = 0
        self._height = 0
        self._durability = 100

    def fix_house(self, tools: Tools):
        """instantiated the given parameter and calls use hammer function on self"""
        tools().use_hammer(self)

    @property
    def durability(self) -> int:
        """Returns durability value on object"""
        return self._durability

    @durability.setter
    def durability(self, new_durability: int) -> None:
        """Sets durability value on object"""

        self._durability = new_durability

    def requires_fixing(self) -> bool:
        """Returns a boolean value which represents whether the object requires fixing
            Checks if durability is below the threshold and returns true if it is
        """
        if self._durability <= 70:
            return True
        else:
            return False
