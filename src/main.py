def main(*args: str) -> int:
    print(f'Got {len(args)} argument(s): {args}')
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(*sys.argv[1:]))
