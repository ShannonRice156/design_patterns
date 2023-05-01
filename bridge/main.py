"""A module to show an example of the bridge design pattern"""
from abc import ABC, abstractmethod


class OS(ABC):
    '''The operating system interface'''
    @abstractmethod
    def screen_width(self) -> None:
        ...

    @abstractmethod
    def screen_height(self) -> None:
        ...

    @abstractmethod
    def screen_resolution(self) -> None:
        ...

    @abstractmethod
    def storage(self) -> None:
        ...


class MacOS(OS):
    """Mac operating system implementer"""

    def screen_width(self) -> int:
        """Return screen width"""
        return 1200

    def screen_height(self) -> int:
        """Return screen height"""
        return 1080

    def screen_resolution(self) -> str:
        """Return screen resolution"""
        return f'{self.screen_width()} x {self.screen_height()}'

    def storage(self) -> str:
        """Return system storage"""
        return "450gb"


class Win(OS):
    """Windows operating system implementer"""

    def screen_width(self) -> int:
        """Return screen width"""
        return 600

    def screen_height(self) -> int:
        """Return screen height"""
        return 600

    def screen_resolution(self) -> str:
        """Return screen resolution"""
        return f'{self.screen_width()} x {self.screen_height()}'

    def storage(self) -> str:
        """Return system storage"""
        return "450gb"


class OSPattern():
    """ A class representing an abstract pattern for determining certain properties of an operating system."""
    @staticmethod
    def get_screen_resolution() -> None:
        os = "macos"
        if os == "macos":
            MacOS().screen_resolution()
        elif os == "windows":
            Win().screen_resolution()


def main() -> None:
    '''Main method which will execute the bridge pattern example code'''

    print(OSPattern.get_screen_resolution())
