"""A module to show an example of the front controller design pattern"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Viewer():
    """A class that represents a viewer and its data"""
    username: str

    def request_access(self, num: int) -> None:
        """Returns whether access is granted for this viewer and this specific page"""
        print(f"Viewer has been granted access to page {num}")
        return "Granted"


class page():
    """A class that represents a page"""

    def __init__(self, num: int) -> None:
        self.num = num

    def view(self) -> None:
        print(f"Page {self.num} is showing")


class pages_controller():
    """A class that holds all the pages and control whether they can be viewed"""

    def __init__(self, pages: list[page]) -> None:
        self.pages = pages

    def view_page(self, num: int, viewer: Viewer) -> None:
        """Tests if the page is accessible and shows the page if it is"""
        if self._accessible(num, viewer):
            self.pages[num - 1].view()
        else:
            print("Access has been denied")

    def _accessible(self, num: int, viewer: Viewer) -> None:
        """Returns whether access can be granted to the viewer given in the parameters"""
        return viewer.request_access(num) == "Granted"


def main() -> None:
    '''Main method which will execute the front controller example'''

    controller = pages_controller([page(1), page(2), page(3)])
    viewer = Viewer(username="Shannon")
    controller.view_page(1, viewer)
