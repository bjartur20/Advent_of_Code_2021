from os import getcwd

def get_gamma_epsilon(data):
    gamma, epsilon = '', ''
    cntrs = [{'0': 0, '1': 1} for _ in range(len(data[0]))]
    for line in data:
        for idx, bit in enumerate(line):
            if bit == '0':
                cntrs[idx]['0'] += 1
            else:
                cntrs[idx]['1'] += 1
    
    for cnt in cntrs:
        if cnt['0'] > cnt['1']:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    
    return int(gamma, 2), int(epsilon, 2)

def main():
    data = [line.strip() for line in open(getcwd()+'/3/input.txt', 'r').readlines()]

    gamma, epsilon = get_gamma_epsilon(data)

    print(gamma * epsilon)
        

if __name__ == "__main__":
    main()