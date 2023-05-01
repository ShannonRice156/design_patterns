'''A module to calculate mathematical equations'''
from .logging import logging as logs


@logs().log
def multiply(*args) -> int:
    '''A method which multiplies the numbers given within the parameters'''
    result = 1
    for arg in args:
        result *= arg

    return result


@logs().log
def add(*args) -> int:
    '''A method which adds the numbers given within the parameters'''
    result = 0
    for arg in args:
        result += arg

    return result


def main() -> None:
    '''Main function which toggles logging on and prints the output of the multiply and add methods'''
    logs().toggle_logging(True)
    print(multiply(2, 3, 4, 5, 6))
    print(add(2, 3, 4, 5, 6))
