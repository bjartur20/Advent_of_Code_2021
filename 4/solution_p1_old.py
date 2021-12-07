from os import getcwd

def parse_input(data):
    nums = [int(i) for i in data[0].split(',')]
    data.pop(0)
    data.pop(0)

    boards = []
    board = []
    for line in data:
        if line == "\n":
            boards.append(board)
            board = []
        else:
            board.append([int(i.strip()) for i in line.split()])

    return nums, boards

def get_best_board(nums, boards):
    earliest_board_wins = []
    for board in boards:
        wins = []
        # Horizontaly
        for line in board:
            if all(num in nums for num in line):
                wins.append(line)
        # Verticaly
        for i in range(len(board)):
            vert = [n[i] for n in board]
            if all(num in nums for num in vert):
                wins.append(vert)
        # Find the row/col with the earliest win
        first_win = []
        last_num_idx = None
        for win in wins:
            curr_last_idx = max([nums.index(i) for i in win])
            if last_num_idx == None or last_num_idx > curr_last_idx:
                last_num_idx = curr_last_idx
                first_win = win
        earliest_board_wins.append(
            {'board': board, 'win': first_win, 'last_num_idx': last_num_idx}
        )

    earliest = None
    for win in earliest_board_wins:
        if earliest == None or earliest['last_num_idx'] > win['last_num_idx']:
            earliest = win
    
    return earliest
        
def get_score(board, marked):
    for n in marked:
        for row in board['board']:
            if n in row:
                row.remove(n)
    
    return sum([sum(i) for i in board['board']]) * board['last_num_idx']

def main():
    data = open(getcwd()+'/4/input.txt', 'r').readlines()

    nums, boards = parse_input(data)

    best_board = get_best_board(nums, boards)

    score = get_score(best_board, nums[:best_board['last_num_idx']+1])

    print(score) # 22545


if __name__ == "__main__":
    main()