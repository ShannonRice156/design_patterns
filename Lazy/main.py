"""A module to show an example of the lazy design pattern"""

from dataclasses import dataclass, field


class fileloader():
    """A class which represents a file loader"""

    def __init__(self, name: str, location: str) -> None:
        self.name = name
        self.location = location

    def get_data(self) -> str:
        """returns the data within the file"""
        return "File data"


@dataclass
class file_list():
    """A class which represents collection of files"""
    files: list = field(default_factory=list)

    def get_data(self, file: fileloader) -> str:
        """Add file to array if its not already added and returns data within file """
        if file not in self.files:
            self.files.append(file)

        return self.files[self.files.index(file)].get_data()


def main():
    """The main function which executes the Lazy design pattern"""

    files = file_list()
    file = fileloader("MyFile", "c:/users/xxx/thisfolder")
    print(files.get_data(file))
