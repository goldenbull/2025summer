
import random

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        if board[row//3*3 + i//3][col//3*3 + i%3] == num:
            return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not is_valid(board, row, col, num) or board[row][col] != 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        board[row][col] = num
    solve(board)
    return board

def remove_numbers(board, num_holes=40):
    holes = 0
    while holes < num_holes:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            holes += 1
    return board

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# 生成完整的数独解
sudoku_board = generate_sudoku()

# 移除部分数字形成谜题
sudoku_puzzle = remove_numbers(sudoku_board, num_holes=40)

# 打印数独谜题
print("生成的数独谜题：")
print_board(sudoku_puzzle)

