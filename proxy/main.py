"""A module to show an example of the proxy design pattern"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    """A class which represents the data of a person"""
    name: str
    age: int


class Room():
    """A class which represents a room"""

    def __init__(self, name: str, age_limit: int) -> None:
        self.occupants = []
        self.name = name
        self.age_limit = age_limit

    def add_occupant(self, person: Person) -> None:
        """Append new person to list of occupants"""
        self.occupants.append(person)


class RoomProxy():
    """A class which represents a room proxy which holds a room and calls its methods if certain conditions are met"""

    def __init__(self, room: Room) -> None:
        self.room = room

    def add_occupant(self, person: Person) -> None:
        """If person given in parameters is of the age to enter this room they are added to the occupants list"""
        if self._check_age(person):
            self.room.add_occupant(person)
            print(f"{person.name} has entered {self.room.name}")
        else:
            print(f"{person.name} is too young to access this room")

    def _check_age(self, person: Person) -> bool:
        """Returns boolean to represent whether the given person is above the age limit of the room on this object"""
        return person.age >= self.room.age_limit


def main() -> None:
    """The main function which executes the proxy design pattern"""
    room = RoomProxy(Room("Bar", 18))
    room.add_occupant(Person(name="Sheila", age=14))
    room.add_occupant(Person(name="John", age=55))
