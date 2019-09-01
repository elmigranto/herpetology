from sys import maxsize as _fake_infinity


def heredoc(multiline: str) -> str:
    lines = multiline.rstrip().strip('\n').split('\n')
    characters_to_trim = min(map(_number_of_leading_space, lines))

    return '\n'.join(map(
        lambda x: x[characters_to_trim:].rstrip(),
        lines
    ))


def single_line(multiline: str) -> str:
    return ' '.join(filter(
        lambda s: len(s) > 0,
        map(str.strip, heredoc(multiline).strip().split('\n'))
    ))


def _number_of_leading_space(string: str) -> int:
    amount = 0

    if string == '':
        return _fake_infinity

    for char in string:
        if char == ' ':
            amount = amount + 1
        else:
            break

    return amount
