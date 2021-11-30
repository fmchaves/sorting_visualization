from resources.sort_algorithm import *
from random import shuffle
from os import system


algorithms_options = {
    'Selection Sort': selectionSort,
    'Selection Sort Extended': selectionSort2,
    'Insertion Sort': insertionSort,
    'Bubble Sort': bubbleSort,
    'Quick Sort': quickSort,
    'Merge Sort': mergeSort
}


def sort(algorithm: str, array: list[int], details: bool = True, kind: str = 'bars'):
    """Sorts the array according to the algorithm

    Args:
        algorithm (str): sort algorithm
        array (list[int]): unsorted array
        details (bool, optional): show details about the sorting proccess. Defaults to True.
        kind (str, optional): show bars or points in the sorting proccess. Defaults to 'bars'.

    Returns:
        [type]: [description]
    """
    algorithm = algorithms_options.get(algorithm, None)

    if algorithm != None:
        algorithm(array, details, kind)
    return None


class InputError(Exception):

    def __init__(self, value, message):
        self.value = value
        self.message = message


def getArrayLength():
    """Asks for the size of the array to sort

    Raises:
        InputError: if the input is not a valid number, raises an error

    Returns:
        [type]: array's size
    """

    while True:
        try:
            n = int(input('Enter the size of the array: '))
            if n < 1:
                system('clear')
                raise InputError(
                    n, 'The size must be an integer greater than zero')
        except InputError as e:
            print(e.message)
        except:
            print('Value must be an integer greater than zero')
        else:
            return n


def chooseSortMethod() -> str:
    """Asks for the sort method

    Raises:        
        InputError: if the input is not a valid number option, raises an error

    Returns:
        str: name pf the method
    """

    sort_options = list(enumerate(algorithms_options.keys(), 1))

    while True:

        print('Chose one of the sort methods below:')

        for index, method_name in sort_options:
            print(f'({index}) {method_name}')

        try:
            method_number = int(input('(number)> '))
            if method_number < 1:
                system('clear')
                raise InputError(
                    method_number, 'Option must be an integer greater than zero')
            if method_number > len(sort_options):
                system('clear')
                raise InputError(
                    method_number, f'Option must be in the interval [1, {len(sort_options)}]')
        except InputError as e:
            print(e.message)
        except:
            print('Option must be an integer greater than zero')
        else:
            return sort_options[method_number - 1][1]


def createRandomArray(length: int = 20) -> list:
    """Creates a random array

    Returns:
        list: a list of numbers
    """

    array = list(range(1, length + 1))
    shuffle(array)
    return array


def main():

    # Asks the user for the size of the list
    n = getArrayLength()
    # Asks the user for the sort method
    method = chooseSortMethod()
    # Creates an unsorted array
    array = createRandomArray(n)
    # Sorts the array
    sort(method, array)


if __name__ == '__main__':
    main()
