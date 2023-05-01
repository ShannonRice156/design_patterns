"""A module to show an example of the momento design pattern"""

from dataclasses import dataclass
from ast import literal_eval


class FileMomento:
    """A class that represents an instance of a file and its state"""

    def __init__(self, state: str) -> None:
        self._state = state

    def get_saved_state(self):
        """Returns the saved state of the file"""
        return self._state


@dataclass
class File():
    """A class which represents all data associated with the file"""
    name: str
    data: str

    def __str__(self) -> str:
        """Override the default string function to return the dictionary string version"""
        return self.__dict__.__str__()

    def save(self) -> FileMomento:
        """returns the file momento associated with the string of self"""
        return FileMomento(self.__str__())

    def restore(self, state: FileMomento) -> None:
        """Restore the file to the state given in its parameters"""
        d = literal_eval(state.get_saved_state())
        self.name = d["name"]
        self.name = d["data"]


def main() -> None:
    """The main function which executes the momento design pattern"""

    states = []
    file1 = File(name="File1", data="dfhjfdhfudhdhfdufhdufhudhfudh")
    states.append(file1.save())

    file1.data = "Hello"
    states.append(file1.save())

    file1.restore(states[0])
