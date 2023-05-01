"""A module to show an example of the singleton design pattern"""


class Books:
    '''Class that holds list of books in a database'''

    def __new__(cls):
        """Creates a new instance of the class if one has not already been made"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(Books, cls).__new__(cls)
            cls.books = ["harry potter", "design patterns", "shrek"]
        return cls.instance


def main() -> None:
    """The main function which executes the singleton design pattern"""

    b = Books()
    print("b length: " + str(len(b.books)))

    b.books.clear()
    print("books cleared")
    print("b length: " + str(len(b.books)))

    d = Books()
    print("d length: " + str(len(d.books)))
