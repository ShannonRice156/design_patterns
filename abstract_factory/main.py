"""A module to show an example of the abstract factory pattern"""

from abc import ABC, abstractmethod
import sorting


class Sort(ABC):
    @abstractmethod
    def sort(self) -> sorting:
        ...


class sorter_factory():
    @abstractmethod
    def get_sorter(self) -> Sort:
        ...


class bubble_sorter_factory():
    def get_sorter(self) -> Sort:
        return BubbleSort


class merge_sorter_factory():
    def get_sorter(self) -> Sort:
        return MergeSort


class quick_sorter_factory():
    def get_sorter(self) -> Sort:
        return QuickSort


class BubbleSort(Sort):
    def sort(self) -> sorting:
        return sorting.bubble


class QuickSort(Sort):
    '''A class that implements the QuickSort algorithm for sorting an array.'''

    def sort(self) -> sorting:
        '''Method that returns an a reference to the sorting.quick method'''
        return sorting.quick


class MergeSort(Sort):
    '''A class that implements the MergeSort algorithm for sorting an array.'''

    def sort(self) -> sorting:
        '''Method that returns an a reference to the sorting.merge method'''
        return sorting.merge


def get_factory(sorting_algorithm: str) -> sorter_factory:
    '''A function that returns the sorting class which is associated with the sorting_algorithm string'''
    if sorting_algorithm == "1":
        return merge_sorter_factory()
    elif sorting_algorithm == "2":
        return quick_sorter_factory()
    elif sorting_algorithm == "3":
        return bubble_sorter_factory()


def get_sorter(sorting_algorithm: int) -> Sort:
    '''Returns the sort function associated with the parameters given'''
    return get_factory(sorting_algorithm).get_sorter()().sort()


def main() -> None:
    '''Main method which will sort list of numbers with the sorting algorithm the user chooses'''
    sorted_ret = None
    while sorted_ret is None:
        nums = [5, 100, 10, 13, 55, 1]
        sorting_algorithm = input(
            f"We will be sorting numbers {nums}. Which sorting algorithm would you like to use? Merge = 1? Quick = 2? or Bubble = 3? ")
        if sorting_algorithm == "1" or sorting_algorithm == "2" or sorting_algorithm == "3":
            sorted_ret = get_sorter(sorting_algorithm)(nums)
        else:
            print("Unrecognised input. Please input the numbers corresponding with the sorting algorithm you wish to use.")

    print(sorted_ret)
