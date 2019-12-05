from . import pycolor
from . import prompt_format

def info(message: str) -> None:
    print(prompt_format.prompt_format(pycolor.Pycolor.GREEN, "*", message))


def add(message: str) -> None:
    print(prompt_format.prompt_format(pycolor.Pycolor.BLUE, "+", message))


def warn(message: str) -> None:
    print(prompt_format.prompt_format(pycolor.Pycolor.PURPLE, "-", message))


def error(message: str) -> None:
    print(prompt_format.prompt_format(pycolor.Pycolor.RED, "!", message))
    print(prompt_format.prompt_format(pycolor.Pycolor.RED, "!", "System terminated"))


def ask(message: str) -> str:
    return input(prompt_format.prompt_format(pycolor.Pycolor.YELLOW, "?", message + " >> "))
