import os

from utils import read_input, parse_measurements, get_larger_than_prev

def main():
    data = read_input(os.getcwd()+'/1/input.txt')
    measurements = parse_measurements(data)
    larger = get_larger_than_prev(measurements)
    print(larger)

if __name__ == "__main__":
    main()