from os import getcwd

from utils import read_input

def main():
    data = read_input(getcwd()+'/2/input.txt')
    
    horizontal, depth = 0, 0

    for line in data:
        direction, movement = line.split()
        if direction == "down":
            depth += int(movement)
        elif direction == "up":
            depth -= int(movement)
        elif direction == "forward":
            horizontal += int(movement)
    print(horizontal)
    print(depth)
    print(horizontal * depth)

if __name__ == "__main__":
    main()