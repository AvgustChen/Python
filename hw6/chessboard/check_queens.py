from random import randint as ri

board = [[0 for i in range(8)],
         [0 for i in range(8)],
         [0 for i in range(8)],
         [0 for i in range(8)],
         [0 for i in range(8)],
         [0 for i in range(8)],
         [0 for i in range(8)],
         [0 for i in range(8)]]


def queens():
    global board
    count = 0
    while count < 8:
        rand = (ri(0, 7), ri(0, 7))
        if board[rand[0]][rand[1]] != '♟️':
            if check_attack(rand):
                board[rand[0]][rand[1]] = '♟️'
                count += 1


def chess_board():
    global board
    for i in range(8):
        for j in range(8):
            if i % 2 == 0 and j % 2 == 0:
                board[i][j] = "⬛"
            elif i % 2 != 0 and j % 2 != 0:
                board[i][j] = "⬛"
            else:
                board[i][j] = "⬜"
    queens()
    for i in board:
        print(*i)


def check_attack(queen):
    global board
    row = queen[0]
    col = queen[1]
    # проверяем горизонталь и вертикаль
    for i in range(len(board)):
        if board[i][col] == '♟️':
            return False
        elif board[row][i] == '♟️':
            return False
    return True
