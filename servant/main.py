"""A module to show an example of the servant design pattern"""

from typing import Protocol


class colour(Protocol):
    """An interface for a representing a colour"""

    def rgb_value(self) -> str:
        ...

    def hex_value(self) -> str:
        ...


class Red():
    """A class which represents the colour red and calculates colour codes"""

    def rgb_value(self) -> str:
        """Returns the rgb value of red"""
        return "255,0,0"

    def hex_value(self) -> str:
        """returns the hex value of red"""
        return "#FF0000"


class Yellow():
    """A class which represents the Colour Yellow and calculates colour codes"""

    def rgb_value(self) -> str:
        """Returns the rgb value of yellow"""
        return "255,255,0"

    def hex_value(self) -> str:
        """Returns the hex value of yellow"""
        return "ffff00"


class green():
    """A class which represents the colour green and calculates colour codes"""

    def rgb_value(self) -> str:
        """Returns the rgb value of green"""
        return "0,255,0"

    def hex_value(self) -> str:
        """Returns the hex value of green"""
        return "00ff00"


class Shape():
    """A class which represents a shape"""

    def __init__(self, width: float, height: float, col: colour) -> None:
        self.width = width
        self.height = height
        self.col = col

    def get_rgb_colour(self) -> str:
        """Return the rgb value of the colour of the shape"""
        return self.col.rgb_value()

    def get_hex_colour(self) -> str:
        """Return the hex value of the colour of the shape"""
        return self.col.hex_value()


class paint():
    """A paint class which paints a given shape and colour"""

    def __init__(self, col: colour) -> None:
        self.col = col

    def paint(self) -> None:
        print(
            f"Painting with colour rgb: {self.get_rgb_paint_colour()} , hex: self.col.hex_value")

    def get_rgb_paint_colour(self) -> str:
        """Returns the rgb value of the colour of the paint object"""
        return self.col.rgb_value()


def main() -> None:
    """The main function which executes the servant design pattern"""

    square = Shape(20, 20, Red())
    square_col = square.get_rgb_colour()
    print(f"rgb: {square_col} , hex: {square.col.hex_value()}")

    painter = paint(Yellow())
    painter.paint()
