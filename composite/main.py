"""A module to show an example of the composite design pattern"""

from abc import ABC, abstractmethod
from decorator_logging.logging import logging


class Filebase(ABC):
    """Abstract base class for any item within the file structure within the file explorer"""
    @abstractmethod
    def size(self):
        ...

    @abstractmethod
    def name(self):
        ...


class File(Filebase):
    """A class which represents a file within the file explorer"""

    def __init__(self, name: str, size: int):
        self._name = name
        self._size = size

    @logging().log
    def size(self) -> int:
        return self._size

    def name(self) -> str:
        return self._name


class Folder(Filebase):
    """A class which represents a folder and its contents within the file explorer"""

    def __init__(self, name: str, files: list[File]):
        self._name = name
        self._items = files
        self._size = 0

    def add_item(self, new_item: Filebase) -> None:
        """Add an item to the contents of this folder"""
        self._items.append(new_item)

    def __calculate_size(self) -> int:
        """Enumerate over all the items within this folder, accumulate the total size and return it"""
        size = 0
        for item in self._items:
            size += item.size()

        return size

    @logging().log
    def size(self) -> int:
        """Return the size of this folder"""
        return self.__calculate_size()

    def name(self) -> str:
        """Return the name of this folder"""
        return self._name


def main() -> None:
    '''Main method which will execute the composite pattern example'''

    folder = Folder("Desktop", [File("List of dates", 20),])
    folder.add_item(File("List of Names", 15))
    folder.add_item(File("List of Colours", 80))
    folder.add_item(
        Folder("My Docs", [File("List of files", 10), File("List of People", 40)]))
    print(folder.size())
