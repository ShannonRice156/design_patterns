"""A module to show an example of the observer design pattern"""

from abc import ABC, abstractmethod
from typing import Protocol


class observable(Protocol):
    """An interface for a observable item"""

    def notify_of_work(self) -> None:
        ...

    def send_home(self) -> None:
        ...

    def fire(self) -> None:
        ...

    def hire(self) -> None:
        ...


class Stocker():
    """A class that represents a stocker"""

    def notify_of_work(self) -> None:
        """Outputs outcome of notification of work"""
        print("Restocker notified that work has come in for them")

    def send_home(self) -> None:
        """Outputs outcome of employee being sent home"""
        print("Restocker was sent home")

    def fire(self) -> None:
        """Outputs outcome of employee being fired"""
        print("A restocker has just been fired.")

    def hire(self) -> None:
        """Outputs outcome of employee being hired"""
        print("A new restocker has been hired.")


class Cleaner():
    """A class that represents a cleaner"""

    def notify_of_work(self) -> None:
        """Outputs outcome of notification of work"""
        print("Cleaner was notified that a mess needs cleaning up")

    def send_home(self) -> None:
        """Outputs outcome of employee being sent home"""
        print("Cleaner was sent home")

    def fire(self) -> None:
        """Outputs outcome of employee being fired"""
        print("A cleaner has just been fired.")

    def hire(self) -> None:
        """Outputs outcome of employee being hired"""
        print("A new cleaner has been hired.")


class CheckoutOperator():
    """A class that represents a checkout operator"""

    def notify_of_work(self) -> None:
        """Outputs outcome of notification of work"""
        print("Checkout operator was notified that there are queues at tills")

    def send_home(self) -> None:
        """Outputs outcome of employee being sent home"""
        print("Checkout operator was sent home")

    def fire(self) -> None:
        """Outputs outcome of employee being fired"""
        print("A checkout operator has just been fired.")

    def hire(self) -> None:
        """Outputs outcome of employee being hired"""
        print("A new checkout operator has been hired.")


class Observer(ABC):
    """Abstract base class for observer objects"""

    def __init__(self, observables: list[observable]) -> None:
        self.observables = observables

    @abstractmethod
    def notify_of_work(self, observable_item: observable) -> None:
        ...

    @abstractmethod
    def send_home(self, observable_item: observable) -> None:
        ...


class StoreManager(Observer):
    """A class that represents a store manager and all their actions"""

    def notify_of_work(self, observable_item: observable) -> None:
        """Loop through observables until parameter given employee is found and notify them of work"""

        for this_employee in self.observables:
            if this_employee == observable_item:
                this_employee.notify_of_work()
                return None

    def send_home(self, observable_item: observable) -> None:
        """Loop through observables until parameter given observable is found and send home"""
        for this_employee in self.observables:
            if this_employee == observable_item:
                observable_item.send_home()
                return None

    def hire(self, observable_item: observable) -> None:
        """Notify employee that they are hired and append them to list of observables"""
        observable_item.hire()
        self.observables.append(observable_item)

    def fire(self, observable_item: observable) -> None:
        """Removes an employee from observables list and notify the observable of being fired"""
        for employee in self.observables:
            if employee == observable_item:
                employee.fire()

        self.observables.remove(observable_item)


def main() -> None:
    """The main function which executes the observer design pattern"""

    cleaner = Cleaner()
    checkout_operator = CheckoutOperator()
    stocker = Stocker()
    manager = StoreManager([cleaner, checkout_operator, stocker])
    manager.notify_of_work(cleaner)

    new_employee = Stocker()
    manager.hire(new_employee)
    manager.notify_of_work(new_employee)
    manager.fire(new_employee)
