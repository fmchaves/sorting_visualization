from time import sleep
import os
from typing import Union


class FontColors:

    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    BLUE = '\033[1;34m'
    YELLOW = '\033[1;33m'
    CYAN = '\033[1;36m'
    BLACK = '\033[1;30m'
    WHITE = '	\033[1;97m'
    DEFAULT = BLUE
    END = '\033[0m'


def getColor(color: str) -> str:

    color = color.upper()
    if hasattr(FontColors, color):
        return getattr(FontColors, color)
    return getattr(FontColors, 'DEFAULT')


def printArray(array: list[int], kind: str = 'bars',  colors: dict = {}, time: float = 0.1) -> None:

    os.system('clear')
    num_digits_max_number = len(str(max(array)))

    for index, number in enumerate(array):

        num_digits_number = len(str(number))
        output = (num_digits_max_number - num_digits_number) * \
            '0' + str(number)
        output += '|'

        if index in colors:
            if kind == 'bars':
                output += number * '='
            else:
                output += (number - 1) * ' ' + '*'
            if colors[index].get('label'):
                output += ' (' + colors[index]['label'] + ')'
            output = getColor(colors[index]['color']) + output
            output += getColor('end')
        else:
            if kind == 'bars':
                output += number * '='
            else:
                output += (number - 1) * ' ' + '*'

        print(output)

    sleep(time)
