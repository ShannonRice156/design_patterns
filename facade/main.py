"""A module to show an example of the facade design pattern"""

from tkinter import *


class WarningText():
    """A class which represents a warning text UI item"""

    def __init__(self, warning_text: str, root: Tk) -> None:
        self.warning_text = warning_text
        self.root = root

    def show(self, placex: int, placey: int):
        """Shows the text at the given x and y coordinates"""
        self.text = Text(self.root, padx=placex, pady=placey)
        self.text.insert(INSERT, self.warning_text)
        self.text.pack()


class WarningButton():
    """A class which represents a warning button UI item"""

    def __init__(self, width: int, height: int, col: str, click_event: object) -> None:
        self._width = width
        self._height = height
        self._colour = col
        self._click_event = click_event

    def show(self, tk: Tk, placex: int, placey: int):
        """Shows the button at the given x and y coordinates"""

        self._button = Button(
            tk, text="OK", bg=self._colour, command=self._click_event)
        self._button.place(x=placex, y=placey,
                           width=self._width, height=self._height)


class WarningWindow():
    """A class which represents a warning window"""

    def __init__(self, warning_message: str) -> None:
        self.warning_message = warning_message
        self.setup()

    def close(self) -> None:
        """Destroy the root TK item"""
        self.root.destroy()

    def setup(self) -> None:
        """This function performs all setup calls that are necessary for this class"""
        self.button = WarningButton(100, 20, "#136F63", self.close)
        self.root = Tk(screenName="Warning")
        self.root.geometry("300x150")
        self.frame = Frame(self.root, border=20)
        self.text = WarningText(self.warning_message, self.root)

    def show(self) -> None:
        """Shows the warning window"""

        self.text.show(50, 30)
        self.button.show(self.root, 180, 110)
        self.root.mainloop(1)


def main() -> None:
    """The main function which executes the facade design pattern"""

    window = WarningWindow("This is a warning")
    window.show()
