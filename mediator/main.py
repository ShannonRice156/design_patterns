"""A module to show an example of the mediator design pattern"""

from typing import Protocol
from dataclasses import dataclass, field


class Lecture(Protocol):
    """An interface for a lecture"""

    def name(self) -> str:
        ...

    def attend_lecture(self, student_name: str) -> None:
        ...


class BiologyLecture():
    """A class representing a biology lecture"""

    def name(self) -> str:
        """Returns the name of the lecture"""
        return "Biology"

    def attend_lecture(self, student_name: str) -> None:
        print(f'{student_name} attended {self.name()} lecture')


class ChemistryLecture():
    def name(self) -> str:
        """Returns the name of the lecture"""
        return "Chemistry"

    def attend_lecture(self, student_name: str) -> None:
        """Notifies that the student has attended the lecture"""
        print(f'{student_name} attended {self.name()} lecture and caused a scene')


class Student(Protocol):
    """An interface for a student"""

    def __init__(self, name: str, age: int) -> None:
        ...

    def attend_lecture(self, lecture_name: Lecture) -> None:
        ...


class BiologyStudent():
    """A class which represents a biology student"""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def attend_lecture(self, lecture: Lecture) -> None:
        lecture.attend_lecture(self.name)


class ChemistryStudent():
    """A class which represents a chemistry student"""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.prepare()

    def prepare(self) -> None:
        """ChemistryStudent prepares for class"""
        print(f"{self.name} is preparing for class")

    def attend_lecture(self, lecture: Lecture) -> None:
        """The student attends the lecture given in partameters then calls self.experiment"""
        lecture.attend_lecture(self.name)
        self.experiment()

    def experiment(self) -> None:
        """Outputs the experiments that the student does"""
        print(f"{self.name} experimented with chemicals")


def main() -> None:
    """The main function which executes the Lazy design pattern"""

    Student1 = BiologyStudent('Shannon', 24)
    Student2 = ChemistryStudent('Lily', 20)
    Student3 = BiologyStudent('Aila', 15)

    Student1.attend_lecture(BiologyLecture())
    Student2.attend_lecture(ChemistryLecture())
    Student3.attend_lecture(BiologyLecture())
