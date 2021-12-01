def read_input(path: str) -> list:
    with open(path, 'r') as f:
        lines = f.readlines()

    return lines

def parse_measurements(measurements: list) -> list:
    return [int(line.strip()) for line in measurements]

def get_larger_than_prev(measurements: list) -> int:
    res = 0
    last = None
    for meas in measurements:
        if last != None and meas > last:
            res += 1
        last = meas

    return res