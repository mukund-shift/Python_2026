# Write your solution here
def who_won(game_board: list):
    ctr1 = 0
    ctr2 = 0
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if game_board[i][j] == 1:
                ctr1 += 1
            elif game_board[i][j] == 2:
                ctr2 += 1
    if ctr1 == ctr2:
        return 0
    elif ctr1 > ctr2:
        return 1
    else:
        return 2