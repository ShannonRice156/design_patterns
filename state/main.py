"""A module to show an example of the state design pattern"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from time import time


@dataclass
class state(ABC):
    """Abstract base class for the state of any ticket"""

    def __init__(self) -> None:
        self.last_updated = time()

    @abstractmethod
    def output(self) -> None:
        ...


class New():
    def output(self) -> None:
        print("This is a new ticket")


class InProgress():
    def output(self) -> None:
        print("This ticket is in progress.")


class Fixed():
    def output(self) -> None:
        print("This ticket is fixed")


@dataclass
class Ticket():
    """ A class which is a representation of a ticket for a ticketing system and holds all ticket related data"""
    num: int
    _status: state = New()

    def update_status(self, status: state) -> None:
        """Update the status variable of this ticket with a new given state"""
        self._status = status

    def output_status(self) -> None:
        """Calls output on status to show the status of the ticket"""
        self._status.output()


def main() -> None:
    """The main function which executes the state design pattern"""

    ticket = Ticket(num=1)
    ticket.output_status()
    ticket.update_status(InProgress())
    ticket.output_status()
    ticket.update_status(Fixed())
    ticket.output_status()
