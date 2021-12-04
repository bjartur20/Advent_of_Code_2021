from os import getcwd

def get_oxygen(data, curr):
    if len(data) == 1:
        return data[0]

    cntrs = [0, 0]

    for line in data:
        bit = line[curr]
        cntrs[int(bit)] += 1
    
    most_common = '1' if cntrs[1] >= cntrs[0] else '0'

    filtered = []
    for line in data:
        if line[curr] == most_common:
            filtered.append(line)

    return get_oxygen(filtered, curr+1)

def get_scrubber(data, curr):
    if len(data) == 1:
        return data[0]

    cntrs = [0, 0]

    for line in data:
        bit = line[curr]
        cntrs[int(bit)] += 1
    
    least_common = '1' if cntrs[1] < cntrs[0] else '0'

    filtered = []
    for line in data:
        if line[curr] == least_common:
            filtered.append(line)

    return get_scrubber(filtered, curr+1)


def main():
    data = [line.strip() for line in open(getcwd()+'/3/input.txt', 'r').readlines()]

    life_support = get_oxygen(data, 0)
    scrubber = get_scrubber(data, 0)

    print(life_support)
    print(scrubber)

    print(int(life_support, 2) * int(scrubber, 2))
        

if __name__ == "__main__":
    main()


# def get_life_support(data):
#     oxygen, scrubber = '', ''
#     oxygen_data = data.copy()
#     scrubber_data = data.copy()
#     cntrs = [{'0': 0, '1': 1} for _ in range(len(data[0]))]

#     while True:
#         for idx, line in enumerate(data):



#     for line in data:
#         for idx, bit in enumerate(line):
#             if bit == '0':
#                 cntrs[idx]['0'] += 1
#             else:
#                 cntrs[idx]['1'] += 1
    
#     for cnt in cntrs:
#         if cnt['0'] > cnt['1']:
#             gamma += '0'
#             epsilon += '1'
#         else:
#             gamma += '1'
#             epsilon += '0'
    
#     return int(gamma, 2), int(epsilon, 2)
