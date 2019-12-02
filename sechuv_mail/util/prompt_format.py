from . import pycolor


def prompt_format(color: str, mark: str, message: str) -> str:
    return "[{color}{mark}{color_end}] {message}".format(color=color, 
                                                         mark=mark, 
                                                         color_end=pycolor.Pycolor.END, 
                                                         message=message)