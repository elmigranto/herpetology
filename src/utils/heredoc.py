from textwrap import dedent


def heredoc(multiline: str) -> str:
    return dedent(multiline).strip()


def single_line(multiline: str) -> str:
    return ' '.join(filter(
        len,
        map(str.strip, multiline.splitlines())
    ))
