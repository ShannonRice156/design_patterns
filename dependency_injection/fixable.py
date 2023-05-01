from typing import Protocol


class fixable(Protocol):
    """An interface which represents a fixable object"""

    @property
    def durability(self) -> int:
        ...

    @durability.setter
    def durability(self, new_durability: int) -> None:
        ...

    def requires_fixing(self) -> bool:
        ...
