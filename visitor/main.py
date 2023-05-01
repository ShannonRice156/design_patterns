"""A module to show an example of the visitor design pattern"""

from __future__ import annotations
from abc import ABC, abstractmethod
from command.main import Vector


class ChessPieceVisitor(ABC):
    """Abstract base class which represents a chess piece visitor"""
    @abstractmethod
    def MoveQueen(self, element: ChessElement) -> None:
        ...

    @abstractmethod
    def MoveKing(self, element: ChessElement) -> None:
        ...

    @abstractmethod
    def MovePawn(self, element: ChessElement) -> None:
        ...

    @abstractmethod
    def MoveCastle(self, element: ChessElement) -> None:
        ...


class ChessVisitor(ChessPieceVisitor):
    """A class which represents a chess visitor"""

    def MoveQueen(self, element: ChessElement) -> None:
        """Moves the queen by 2 in both x and y direction"""
        element.position.x += 2
        element.position.y += 2
        print("Moving the Queen.")

    def MoveKing(self, element: ChessElement) -> None:
        """Move the king in the y direction by 1"""
        element.position.y += 1
        print("Moving the king.")

    def MovePawn(self, element: ChessElement) -> None:
        """Move the pawn in the y direction by 1"""
        element.position.y += 1
        print("Moving the pawn")

    def MoveCastle(self, element: ChessElement) -> None:
        """Move the castle in the x direction by 3"""
        element.position.x += 3
        print("Moving the castle.")


class ChessCaptureVisitor:
    """A class which represents a chess capture visitor"""

    def MoveQueen(self, element: ChessElement) -> None:
        """Outputs the outcome of the queen being moved and captured"""
        print(
            f"The Queen has been captured at position {element.position.x}, {element.position.y}")

    def MoveKing(self, element: ChessElement) -> None:
        """Outputs the outcome of the king being moved and captured"""
        print(
            f"The King has been captured at position {element.position.x}, {element.position.y}")

    def MovePawn(self, element: ChessElement) -> None:
        """Outputs the outcome of the pawn being moved and captured"""
        print(
            f"A pawn has been captured at position {element.position.x}, {element.position.y}")

    def MoveCastle(self, element: ChessElement) -> None:
        """Outputs the outcome of the castle being moved and captured"""
        print(
            f"A castle has been captured at position {element.position.x}, {element.position.y}")


class ChessElement(ABC):
    """Abstract base class which represents a chess element"""

    def __init__(self, position: Vector) -> None:
        self.position = position

    @abstractmethod
    def accept(self, visitor: ChessVisitor) -> None:
        ...


class Queen(ChessElement):
    """A class which represents a Queen chess piece"""

    def accept(self, visitor: ChessVisitor) -> None:
        """Calls visitor to move the Queen"""
        visitor.MoveQueen(self)


class King(ChessElement):
    """A class which represents a King chess piece"""

    def accept(self, visitor: ChessVisitor) -> None:
        """Calls visitor to move the King"""
        visitor.MoveKing(self)


class pawn(ChessElement):
    """A class which represents a pawn chess piece"""

    def accept(self, visitor: ChessVisitor) -> None:
        """Calls visitor to move the pawn"""
        visitor.MovePawn(self)


class Castle(ChessElement):
    """A class which represents a castle chess piece"""

    def accept(self, visitor: ChessVisitor) -> None:
        """Calls visitor to move the castle"""
        visitor.MoveCastle(self)


class ChessGame():
    """A class to represent a chess game"""

    def __init__(self, pieces: list[ChessElement]):
        self.pieces = pieces

    def accept(self, visitor: ChessVisitor):
        """Accepts the visitor piece and calls accept for each element in pieces"""
        for pieces in self.pieces:
            pieces.accept(visitor)


def main() -> None:
    """The main function which executes the visitor design pattern"""

    pieces = [King(Vector(x=1, y=1)), Queen(Vector(x=5, y=5)),
              pawn(Vector(x=3, y=5)), Castle(Vector(10, 10))]
    game = ChessGame(pieces)
    game.accept(ChessVisitor())
    game.accept(ChessCaptureVisitor())
