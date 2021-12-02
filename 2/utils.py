def read_input(path: str) -> list:
    data = open(path, 'r').readlines()

    return [line.strip() for line in data]