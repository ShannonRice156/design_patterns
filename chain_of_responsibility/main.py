"""A module to show an example of the chain of responsibility design pattern"""

from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Self
from dataclasses import dataclass


class ailment_area(Enum):
    """Enumeration for the area of the ailment"""

    head = auto()
    legs = auto()
    chest = auto()
    aches = auto()


@dataclass
class Patient():
    """A class which holds all the data on the patient"""
    area_of_concern: ailment_area
    name: str
    age: int
    treated: bool = False


class MedicalPersonnel(ABC):
    """Abstract base class for medical personnel"""

    def __init__(self, referral_personnel: Self) -> None:
        self.referral_personnel = referral_personnel
        super().__init__()

    def refer(self, patient: Patient) -> None:
        """Refer the patient given in the parameters to another medical personnel"""
        if self.referral_personnel is not None:
            self.referral_personnel.treat(patient)

    @abstractmethod
    def treat(self, patient: Patient) -> None:
        ...


class heart_surgeon(MedicalPersonnel):
    """A class representing a heart surgeon"""

    def treat(self, patient: Patient) -> None:
        """If the area of concern is specific to this doctor this patient will be treated otherwise they are referred to another medical personnel"""
        if patient.area_of_concern == ailment_area.chest:
            print("Patient treated by Heart surgeon")
            patient.treated = True
        else:
            self.refer(patient)


class brain_surgeon(MedicalPersonnel):
    """A class representing a brain surgeon"""

    def treat(self, patient: Patient) -> None:
        """If the area of concern is specific to this doctor this patient will be treated otherwise they are referred to another medical personnel"""

        if patient.area_of_concern == ailment_area.head:
            print("Patient treated by Brain surgeon")
            patient.treated = True
        else:
            self.refer(patient)


class GP(MedicalPersonnel):
    """A class representing a GP"""

    def treat(self, patient: Patient) -> None:
        """If the area of concern is specific to this doctor this patient will be treated otherwise they are referred to another medical personnel"""

        if patient.area_of_concern == ailment_area.aches:
            print("Patient treated by GP")
            patient.treated = True
        else:
            self.refer(patient)


class Hospital():
    """A class representing a hospital and the patients and doctors within it"""

    def __init__(self) -> None:
        self.patients = {}
        self.heart_surgeon = heart_surgeon(None)
        self.brain_surgeon = brain_surgeon(self.heart_surgeon)
        self.gp = GP(self.brain_surgeon)

    def treat_patient(self, patient: Patient) -> None:
        """Add patient to list of hosptial patients and start by having the gp attempt to treat them"""
        self.patients[patient.name] = patient
        self.gp.treat(patient)

    def show_outcome(self, patient: Patient) -> None:
        """Print whether the patient has been treated or not"""
        if self.patients[patient.name].treated:
            print("Patient Successfully Treated")
        else:
            print("Patient could not be treated at this hospital")


def main() -> None:
    '''Main method which will execute the chain of responsibility pattern example'''

    patient = Patient(name="Joseph", age=30,
                      area_of_concern=ailment_area.chest)
    hospital = Hospital()
    hospital.treat_patient(patient)
    hospital.show_outcome(patient)

    patient2 = Patient(name="Joseph", age=30,
                       area_of_concern=ailment_area.legs)
    hospital.treat_patient(patient2)
    hospital.show_outcome(patient2)
