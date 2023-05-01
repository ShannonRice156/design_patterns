"""A module to show an example of the dependency injection design pattern"""

from .tools import Tools
from .house import House


def main():
    """The main function which executes the design pattern"""
    h = House()
    h.width = 50.0
    h.height = 50.0
    h.durability = 50
    h.fix_house(Tools)
