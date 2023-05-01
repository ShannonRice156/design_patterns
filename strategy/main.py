"""A module to show an example of the strategy design pattern"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class material(ABC):
    """A class that holds all data and functions associated with material"""
    units: int
    price: float
    multiplier: int = 1.2

    @abstractmethod
    def cost(self) -> float:
        ...


class TopQualityMaterial(material):
    """A class representing a high quality material type and calculating its cost"""

    def cost(self) -> float:
        """Returns the cost of the material based on the units, price and multiplier"""
        return self.units * self.price * self.multiplier


class BasicMaterial(material):
    def calculate_multiplier(self) -> float:
        """Returns a discounted multiplier if the units are more than 10"""
        if (self.units > 10) and (self.multiplier > 2):
            return self.multiplier - 0.5

        return self.multiplier

    def cost(self) -> float:
        """Returns the cost of the material based on units, price and multiplier"""
        return self.units * self.price * self.calculate_multiplier()


class BuildType(Protocol):
    """An interface for a build type"""

    def cost(self, material_price: float) -> float:
        ...

    def __str__(self) -> str:
        ...


class BuildHouse:
    def __init__(self, build_type: BuildType, materials: material):
        self.materials = materials
        self.build_type = build_type

    def price(self) -> float:
        return self.build_type.cost(self.materials.cost())


class Mansion():
    def cost(self, material_prices: float) -> float:
        return material_prices * 2

    def __str__(self) -> str:
        return "Mansion"


class House():
    def cost(self, material_prices: float) -> float:
        return material_prices * 1.2

    def __str__(self) -> str:
        return "House"


def check_quote(quote: BuildHouse) -> None:
    response = ""
    while ((response != "y") and (response != "n")):
        response = input(
            f"The quote for this f{quote.build_type}build is f{quote.price()}. Would you like to reduce the cost with basic materials instead of top quality? y/n")

    if response == "n":
        print("House has been built")
    else:
        quote.materials = BasicMaterial(quote.materials.units, 5)
        response2 = input(
            f"With lesser materials the price is {quote.price()}. Would you like to build? y/n")

        if response2 == "y":
            print("House has been built")
        else:
            print("We are sorry we could not help you today")


def main() -> None:
    """The main function which executes the strategy design pattern"""

    house = House()
    mansion = Mansion()

    quote1 = BuildHouse(house, TopQualityMaterial(50, 10, 3))
    quote2 = BuildHouse(mansion, TopQualityMaterial(200, 10, 1.5))

    check_quote(quote1)
    check_quote(quote2)
