from textwrap import dedent
from typing import TypeVar
from pprint import pprint

T = TypeVar('T')


def heredoc(multiline: str) -> str:
    return dedent(multiline).strip()


def single_line(multiline: str) -> str:
    return ' '.join(filter(
        len,
        map(str.strip, multiline.splitlines())
    ))


def pp(anything: T) -> T:
    pprint(anything)
    return anything
