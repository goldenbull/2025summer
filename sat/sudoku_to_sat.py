with open("problems/百分号数独游戏格局文件（设计要求的应用任务）/%-sudoku.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  # 跳过前2行，读取剩余所有行

n = -1
line_n = lines[n]
list_cnf = []


# 空白棋盘

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

ranges = rows + cols + boxes + pcf_boxes + cross_line
for rng in ranges:
    # 每个格子可以是1到9
    for x, y in rng:
        list_cnf.append(tuple(x * 100 + y * 10 + v for v in range(1, 10)))

    # 1到9只能出现1次
    for v in range(1, 10):
        for i in range(9):
            for j in range(i + 1, 9):
                (r1, c1), (r2, c2) = rng[i], rng[j]
                list_cnf.append((-r1 * 100 - c1 * 10 - v, -r2 * 100 - c2 * 10 - v))

# 读入已有的数字
curr_numbers = []
for i in range(9):
    for j in range(9):
        c = line_n[9 * i + j]
        if c != '.':
            curr_numbers.append((i, j, int(c)))

# 已填入的数字转为cnf
for x, y, v in curr_numbers:
    list_cnf.append((100 * (x + 1) + 10 * (y + 1) + v,))

# 输出到cnf文件
literals = set()
for cnf in list_cnf:
    for v in cnf:
        literals.add(abs(v))

clauses = sorted(set(list_cnf))

fout = open("e:/workspace/s.cnf", "wt")
fout.write("c sudoku output\n")
fout.write(f"p cnf {len(literals)} {len(clauses)}\n")
for clause in clauses:
    for l in clause:
        print(l, end=' ', file=fout)
    print(0, file=fout)

fout.close()
