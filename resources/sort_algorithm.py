__all__ = ['selectionSort', 'selectionSort2',
           'insertionSort', 'bubbleSort', 'quickSort', 'mergeSort']

from resources.custom_output import printArray


def selectionSort(array: list[int], details: bool = True, kind: str = 'bars') -> None:
    """Sorts the list according to the selection algorithm"""

    for reference in range(len(array) - 1):
        min_index = reference
        for current in range(reference + 1, len(array)):
            if array[current] < array[min_index]:
                min_index = current
            if details:
                printArray(
                    array, kind, {
                        reference: {'color': 'red', 'label': 'REFERENCE'},
                        current: {'color': 'green', 'label': 'CURRENT'}}, 0.2)
            else:
                printArray(array, kind, {}, 0.05)
        array[reference], array[min_index] = array[min_index], array[reference]

    printArray(array, kind, {}, 0.05)


def selectionSort2(array: list[int], details: bool = True, kind: str = 'bars') -> None:
    """Sorts the list according to selection sort algorithm

    Args:
        array (list[int]): unsorted list
        details (bool, optional): show details about the sorting proccess. Defaults to True.
        kind (str, optional): show bars or points. Defaults to 'bars'.

    Raises:
        Exception: if array's length is less than 4, raises an error
    """

    if len(array) < 4:
        raise Exception('simpleSort2: Array length must be greater than 4')

    start, end = 0, len(array) - 1

    while start < end:
        for i, j in zip(range(start + 1, end), range(end - 1, start, -1)):
            if i != j and array[i] < array[start]:
                array[i], array[start] = array[start], array[i]
            if i != j and array[j] > array[end]:
                array[j], array[end] = array[end], array[j]
            if details:
                printArray(
                    array, kind, {
                        start: {'color': 'red', 'label': 'REFERENCE - MIN'},
                        i: {'color': 'green', 'label': 'MIN'},
                        end: {'color': 'blue', 'label': 'REFERENCE - MAX'},
                        j: {'color': 'yellow', 'label': 'MAX'}}, 0.2)
            else:
                printArray(array, kind, {}, 0.05)

        start += 1
        end -= 1
    if array[start - 1] > array[end + 1]:
        array[start - 1], array[end + 1] = array[end + 1], array[start - 1]

    printArray(array, kind, {}, 0.05)


def insertionSort(array: list[int], details: bool = True, kind: str = 'bars') -> None:
    """Sort's the array according to the insertion sort algorithm

    Args:
        array (list[int]): unsorted list
        details (bool, optional): show details about the sorting proccess. Defaults to True.
        kind (str, optional): show bars or points. Defaults to 'bars'.
    """

    for to_right in range(1, len(array)):
        for to_left in range(to_right, 0, -1):
            if details:
                printArray(
                    array, kind, {
                        to_left - 1: {'color': 'red', 'label': 'ADJACENT'},
                        to_left: {'color': 'green', 'label': 'CURRENT'}}, 0.2)
            else:
                printArray(array, kind, {}, 0.1)
            if array[to_left] < array[to_left - 1]:
                array[to_left], array[to_left -
                                      1] = array[to_left - 1], array[to_left]
            else:
                break

    printArray(array, kind, {}, 0.1)


def bubbleSort(array: list[int], details: bool = True, kind: str = 'bars') -> None:
    """Sort's the array according to the bubble sort algorithm

    Args:
        array (list[int]): unsorted list
        details (bool, optional): show details about the sorting proccess. Defaults to True.
        kind (str, optional): show bars or points. Defaults to 'bars'.
    """

    for i in range(1, len(array)):
        for current in range(len(array) - i):
            if array[current] > array[current + 1]:
                array[current], array[current +
                                      1] = array[current + 1], array[current]
            if details:
                printArray(
                    array, kind, {
                        current + 1: {'color': 'red', 'label': 'CURRENT-MAX'},
                        current: {'color': 'green', 'label': 'ADJACENT'}}, 0.2)
            else:
                printArray(array, kind, {}, 0.1)

    printArray(array, kind, {}, 0.1)


def quickSort(array: list[int], details: bool = True, kind: str = 'bars') -> None:
    """Sort's the array according to the quick sort algorithm

    Args:
        array (list[int]): unsorted list
        details (bool, optional): show details about the sorting proccess. Defaults to True.
        kind (str, optional): show bars or points. Defaults to 'bars'.
    """

    def partition(array: list[int], low: int, high: int) -> int:

        pivot_value = array[high]
        index = low - 1

        for k in range(low, high):
            if array[k] < pivot_value:
                index += 1
                array[k], array[index] = array[index], array[k]
            if details:
                printArray(
                    array, kind, {
                        low: {'color': 'red', 'label': 'START'},
                        high: {'color': 'green', 'label': 'END-PIVOT'},
                        k: {'color': 'blue', 'label': 'CURRENT'}})
            else:
                printArray(array, kind, {}, 0.1)

        if pivot_value < array[index + 1]:
            array[index + 1], array[high] = array[high], array[index + 1]
        return index + 1

    def sort(array: list[int], low: int, high: int):

        if low < high:

            pivot_index = partition(array, low, high)

            sort(array, low, pivot_index - 1)
            sort(array, pivot_index + 1, high)

    sort(array, 0, len(array) - 1)

    printArray(array, kind, {}, 0.1)


def mergeSort(array: list[int], details: bool = True, kind: str = 'bars'):
    """Sort's the array according to the merge sort algorithm

    Args:
        array (list[int]): unsorted list
        details (bool, optional): show details about the sorting proccess. Defaults to True.
        kind (str, optional): show bars or points. Defaults to 'bars'.
    """

    def mergeSortInner(array: list[int], start_index: int, end_index: int):

        if (end_index - start_index) > 1:

            middle_index = (end_index + start_index) // 2

            mergeSortInner(array, start_index, middle_index)
            mergeSortInner(array, middle_index, end_index)

            temp = [None] * (end_index - start_index)
            i, j, k = start_index, middle_index, 0

            while i < middle_index and j < end_index:
                if array[i] < array[j]:
                    temp[k] = array[i]
                    i += 1
                else:
                    temp[k] = array[j]
                    j += 1
                k += 1

            while i < middle_index:
                temp[k] = array[i]
                k += 1
                i += 1

            while j < end_index:
                temp[k] = array[j]
                k += 1
                j += 1

            for i in range(start_index, end_index):
                aux = temp[i - start_index]
                if aux != None:
                    array[i] = aux

            if details:
                printArray(
                    array, kind, {
                        start_index: {'color': 'red', 'label': 'START'},
                        middle_index: {'color': 'blue', 'label': 'MIDDLE'},
                        end_index - 1: {'color': 'green', 'label': 'END'}}, 0.3)
            else:
                printArray(array, kind, {}, 0.2)

    mergeSortInner(array, 0, len(array))

    printArray(array, kind)
