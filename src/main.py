def main(*args: str) -> int:
    print(f'Got {len(args)} argument(s): {args}')
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(*sys.argv))
else:
    from utils.heredoc import single_line
    raise RuntimeError(single_line('''
        This module is not supposed to be imported.
        Run directly with python.
    '''))
