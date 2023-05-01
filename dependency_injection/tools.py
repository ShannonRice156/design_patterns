from abc import ABC, abstractmethod
from enum import Enum
from .fixable import fixable


class HammerType(Enum):
    """Enumeration for hammer type"""

    sledgehammer = 1
    claw = 2
    club = 3


class Tool(ABC):
    """Abstract base class which represents a tool"""
    @abstractmethod
    def price(self) -> int:
        ...

    @abstractmethod
    def name(self) -> int:
        ...

    @abstractmethod
    def type(self) -> int:
        ...

    @abstractmethod
    def fix_item(self, item: object) -> int:
        ...


class Hammer(Tool):
    """A class which represents a hammer tool"""

    def __init__(self, type: HammerType) -> None:
        self._type = type
        self._durability = 100
        super().__init__()

    def price(self) -> int:
        """Returns the price of the hammer"""
        return 50.0

    def type(self) -> HammerType:
        """Returns the type of hammer"""
        return self._type

    def name(self) -> int:
        """Returns the name of the hammer"""
        return "Hector"

    def fix_item(self, item: object) -> None:
        """Resets item durability if it is determined that fixing is needed"""
        amount_needed = (100 - item.durability)
        if item.requires_fixing() and (self.durability >= amount_needed):
            self.durability += - amount_needed
            item.durability = 100

    @property
    def durability(self) -> int:
        """Returns durability value on object"""
        return self._durability

    @durability.setter
    def durability(self, new_durability: int) -> None:
        """Sets durability value on object"""
        self._durability = new_durability

    def requires_fixing(self) -> bool:
        if self.durability < 30:
            return True
        else:
            return False


class Tools():
    """A class which holds all the tools"""

    def __init__(self) -> None:
        self._hammer = Hammer(HammerType.sledgehammer)
        print("Tools have been setup")  # replace with logging

    def use_hammer(self, obj: fixable) -> None:
        """Function that passes object through to the correct tool and fixes the item"""
        self._hammer.fix_item(obj)
        print("Using " + str(type))
