import copy
import random


# 目标生成一个数独，打印出来并生成数独文件

def get_box(r, c):
    return [(i, j)
            for i in range(r, r + 3)
            for j in range(c, c + 3)
            ]


rows = [[(r, c) for c in range(1, 10)] for r in range(1, 10)]
cols = [[(r, c) for r in range(1, 10)] for c in range(1, 10)]
boxes = [get_box(r, c) for r in [1, 4, 7] for c in [1, 4, 7]]
pcf_boxes = [get_box(2, 2), get_box(6, 6)]
cross_line = [[(r, 10 - r) for r in range(1, 10)]]


# 打印棋盘
def print_borad(sudoku):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("---------------------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + ' ', end="")


# 判断（row,col)处的数字是否有效,对应矩阵位置sudoku[row-1][col-1]
def is_valid(sudoku, row, col, value):
    # 检查行约束
    for i in range(9):
        if sudoku[row - 1][i] == value:
            return False
    # 检查列约束
    for j in range(9):
        if sudoku[j][col - 1] == value:
            return False
    # 检查九宫格约束
    x, y = 3 * ((row - 1) // 3), 3 * ((col - 1) // 3)
    for i in range(3):
        for j in range(3):
            if sudoku[x + i][y + j] == value:
                return False
    # 检查百分号约束
    if (row, col) in pcf_boxes:
        x = 1 if (row + col) < 10 else 5
        for i in range(3):
            for j in range(3):
                if sudoku[x + i][x + j] == value:
                    return False
    if (row, col) in cross_line:
        for i in range(9):
            if sudoku[i][8 - i] == value:
                return False
    return True


# 回溯法解数独
def solve_sudoku(sudoku):
    for row in range(1, 10):
        for col in range(1, 10):
            if sudoku[row-1][col-1] == 0:
                for value in random.sample(range(1,10),9):  # 随机尝试数字
                    if is_valid(sudoku, row, col, value):  # 满足约束
                        sudoku[row-1][col-1] = value
                        if solve_sudoku(sudoku):  # 若合法，递归处理填好该格子后的数独
                            return True  # 递归返回真，找到解，直接返回
                        else:
                            sudoku[row-1][col-1] = 0  # 无解，重置当前格子为0，尝试下一个数字
                return False
    return True


# 每个格子的当前状态
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = 0
        self.candidates = set(range(1, 10))  # 允许填入的数字


board = {(x, y): Cell(x, y)
         for x in range(1, 10)
         for y in range(1, 10)}


# 给一个格子赋值时处理相关约束
def set_value(row, col, value):
    board[(row, col)].value = value
    # 处理行和列的其他格子
    for cell in board.values():
        if cell.row == row or cell.col == col:
            if value in cell.candidates and cell.value == 0:
                cell.candidates.remove(value)
    # 处理九宫格内其他格子
    box_row = ((row - 1) // 3) * 3 + 1
    box_col = ((col - 1) // 3) * 3 + 1
    for i in range(3):
        for j in range(3):
            cell = board[(box_row + i), (box_col + j)]
            if cell.value == 0 and value in cell.candidates:
                cell.candidates.remove(value)
    # 处理百分号内其他格子
    if (row, col) in pcf_boxes:
        m = 2 if (row + col) < 10 else 6
        for i in range(3):
            for j in range(3):
                cell = board[(m + i), (m + j)]
                if cell.value == 0 and value in cell.candidates:
                    cell.candidates.remove(value)
    #处理对角线上其他格子
    if (row, col) in cross_line:
        for i in range(1,10):
            cell = board[(i,10-i)]
            if cell.value == 0 and value in cell.candidates:
                cell.candidates.remove(value)

# 随机填入一个格子
def fill_one_cell():
    empty_cells = [c for c in board.values() if c.value == 0]
    selected_cell = random.choice(empty_cells)
    value = random.choice(list(selected_cell.candidates))
    set_value(selected_cell.row, selected_cell.col, value)


# 生成一个完整数独
def complete_sudoku():
    sudoku = [[0] * 9 for i in range(9)]
    for i in range(20):
        fill_one_cell()
    solve_sudoku(sudoku)
    return sudoku

my_sudoku=complete_sudoku()
print_borad(my_sudoku)

#挖洞
def dig_holes(sudoku,holes):
    cells = [(i,j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    for i,j in cells[:holes]:
        sudoku[i][j] = 0
    return sudoku

#生成挖洞后的数独
print("\n")
holes_num = random.randint(30,40)
dig_holes(my_sudoku, holes_num)
print_borad(my_sudoku)

#生成数独文件
print("\n")
sudoku_list=[]
for row in my_sudoku:
    for num in row:
        sudoku_list.append('.' if num==0 else str(num))
result=''.join(sudoku_list)
print(result)
fout = open("e:/workspace/my_sudoku.txt", "wt")
fout.write(result)
fout.close()