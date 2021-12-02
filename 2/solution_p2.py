from os import getcwd

def main():
    data = [line.strip() for line in open(getcwd()+'/2/input.txt', 'r').readlines()]

    horizontal, depth, aim = 0, 0, 0
    changes = lambda x, y: 

    for line in data:
        direction, movement = line.split()
        if direction == "down":
            aim += int(movement)
        elif direction == "up":
            aim -= int(movement)
        elif direction == "forward":
            horizontal += int(movement)
            depth += aim * int(movement)
    
    print(horizontal * depth)

if __name__ == "__main__":
    main()