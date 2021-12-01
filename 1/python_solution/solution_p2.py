from os import getcwd

from utils import read_input, parse_measurements, get_larger_than_prev

def parse_to_window_sums(measurements: list) -> list:
    res = []
    for idx in range(len(measurements)):
        if idx == len(measurements)-2: break
        
        res.append(sum(
            (measurements[idx],
            measurements[idx+1],
            measurements[idx+2])
        ))

    return res

def main():
    data = read_input(getcwd()+'/1/input.txt')
    measurements = parse_measurements(data)
    windows = parse_to_window_sums(measurements)
    larger = get_larger_than_prev(windows)
    print(larger)

if __name__ == "__main__":
    main()