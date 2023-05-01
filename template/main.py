"""A module to show an example of the template design pattern"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
import time


class AnimalSpecies(Enum):
    """Enumeration for different animal species"""

    lion = auto()
    peacock = auto()
    tiger = auto()
    monkey = auto()


@dataclass
class animal_enclosure():
    """dataclass to hold all information about the animal enclosure"""

    species: AnimalSpecies
    thirsty: bool = True
    clean: bool = False
    _feed_time: int = 0

    def feed(self) -> None:
        """Reset feed time to current time"""
        self._feed_time = time.time()

    def time_since_fed(self) -> float:
        """Calculate time since fed by using the current time and last feed time"""
        return time.time() - self._feed_time


class Zoologist(ABC):
    """Abstract base class for a zoologist."""

    def care_for_animals(self):
        """Execute functionality to care for animals"""

        self.feed_animals()
        self.give_animals_water()
        self.clean_animals()
        self.socialise_with_animals()

    @abstractmethod
    def feed_animals(self) -> None:
        ...

    @abstractmethod
    def give_animals_water(self) -> None:
        ...

    @abstractmethod
    def clean_animals(self) -> None:
        ...

    @abstractmethod
    def socialise_with_animals(self) -> None:
        ...


class LionKeeper(Zoologist):
    """A class representing a lion keeper, who is a type of zoologist"""

    def __init__(self) -> None:
        self.animals = animal_enclosure(species=AnimalSpecies.lion)

    def feed_animals(self) -> None:
        if self.animals.time_since_fed() >= 1:
            print("The lion keeper throws meat into the lion enclosure")
            self.animals.feed()

    def give_animals_water(self) -> None:
        if self.animals.thirsty:
            print("The lion keeper has filled the water for the lions")
            self.animals.thirsty = False

    def clean_animals(self):
        if self.animals.clean == False:
            self.animals.clean = True
            print("Lion keeper has cleaned the animals")

    def socialise_with_animals(self):
        print("The lions do not require human socialising")


class MonkeyKeeper(Zoologist):
    """A class representing a monkey keeper, who is a type of zoologist"""

    def __init__(self) -> None:
        self.animals = animal_enclosure(species=AnimalSpecies.monkey)

    def feed_animals(self) -> None:
        if self.animals.time_since_fed() >= 5:
            print("The Monkey keeper gives the monkeys bananas")
            self.animals.feed()

    def give_animals_water(self) -> None:
        if self.animals.thirsty:
            print("The Monkey keeper has filled the water for the Monkeys")
            self.animals.thirsty = False

    def clean_animals(self):
        if self.animals.clean is False:
            self.animals.clean = True
            print("Monkey keeper has cleaned the animals")

    def socialise_with_animals(self):
        print("The Monkey keeper plays with the monkeys to get them used to human contact")


def main():
    """The main function which executes the template design pattern"""

    print("Start of zoo day")
    lion_keeper = LionKeeper()
    monkey_keeper = MonkeyKeeper()

    lion_keeper.care_for_animals()
    monkey_keeper.care_for_animals()
    time.sleep(4)

    lion_keeper.care_for_animals()
    monkey_keeper.care_for_animals()
    print("End of zoo day")
