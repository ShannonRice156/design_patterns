"""A module to show an example of the delegation design pattern"""

from dataclasses import dataclass
from abc import abstractmethod
from typing import Protocol


class Output(Protocol):
    """An interface which represents an output"""
    @abstractmethod
    def print(self, printable_str: str):
        ...


class OutputNormal():
    """A class that represents a normal printing output"""

    def print(self, printable_str: str) -> None:
        """Print the given string"""
        print(printable_str)


class OutputAdvanced():
    """A class that represents a advanced printing output"""

    def print(self, printable_str: str) -> None:
        """format the given string and print"""
        printable_list = printable_str.split(",")
        for l in printable_list:
            print(f"    {l.strip()}")


@dataclass(frozen=True)
class Animal():
    """A class which holds all data associated with an Animal"""

    name: str
    age: int


@dataclass(frozen=True)
class Dog(Animal):
    """A class which holds all data associated with a dog"""

    breed: str

    def print_values(self, output: Output) -> None:
        """Calls the print function on the Output parameter given"""
        output.print(f"Name: {self.name},Age: {self.age},Breed: {self.breed}")


def main() -> None:
    """The main function which executes the delegation design pattern"""

    d = Dog(name="Peter", age=10, breed="Dauchund")
    d.print_values(OutputNormal())
    d.print_values(OutputAdvanced())
