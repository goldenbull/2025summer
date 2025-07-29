with open("problems/百分号数独游戏格局文件（设计要求的应用任务）/%-sudoku.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()[2:]  # 跳过前2行，读取剩余所有行

n = 0
line_n = lines[n]
list_cnf = []


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
exit()

# 格约束
for i in range(1, 10):
    for j in range(1, 10):
        list_cnf.append([100 * i + 10 * j + k for k in range(1, 10)])
        for k1 in range(1, 10):
            for k2 in range(k1 + 1, 10):
                list_cnf.append([-100 * i - 10 * j - k1, -100 * i - 10 * j - k2])

# 行约束
# 每行包含1-9
for row in rows:
    for k in range(1, 10):
        list_cnf.append([100 * r + 10 * c + k for (r, c) in row])
# 同一行不能包含重复数字
for row in rows:
    for i in range(9):
        for j in range(i + 1, 9):
            (r1, c1), (r2, c2) = row[i], row[j]
            for k in range(1, 10):
                list_cnf.append([-r1 * 100 - c1 * 10 - k, -r2 * 100 - c2 * 10 - k])

# 列约束
# 每列包含1-9
for col in cols:
    for k in range(1, 10):
        list_cnf.append([100 * r + 10 * c + k for (r, c) in col])
# 同一列不能包含重复数字
for col in cols:
    for i in range(9):
        for j in range(i + 1, 9):
            (r1, c1), (r2, c2) = col[i], col[j]
            for k in range(1, 10):
                list_cnf.append([-r1 * 100 - c1 * 10 - k, -r2 * 100 - c2 * 10 - k])

# 盒子约束
# 每九宫格包含1-9
for box in boxes:
    for k in range(1, 10):
        list_cnf.append([100 * r + 10 * c + k for (r, c) in box])
# 同一九宫格不能包含重复数字
for box in boxes:
    for i in range(9):
        for j in range(i + 1, 9):
            (r1, c1), (r2, c2) = box[i], box[j]
            for k in range(1, 10):
                list_cnf.append([-r1 * 100 - c1 * 10 - k, -r2 * 100 - c2 * 10 - k])

# 百分号约束
# 窗口包含1-9
for box in pcf_boxes:
    for k in range(1, 10):
        list_cnf.append([100 * r + 10 * c + k for (r, c) in box])
# 不能有重复数字
for box in pcf_boxes:
    for i in range(9):
        for j in range(i + 1, 9):
            (r1, c1), (r2, c2) = box[i], box[j]
            for k in range(1, 10):
                list_cnf.append([-r1 * 100 - c1 * 10 - k, -r2 * 100 - c2 * 10 - k])

# 斜对角线
line_range = [19, 28, 37, 46, 55, 64, 73, 82, 91]
for k in range(1, 10):
    list_cnf.append([10 * x + k for x in line_range])
for i in range(len(line_range)):
    for j in range(i + 1, len(line_range)):
        x1 = line_range[i]
        x2 = line_range[j]
        for k in range(1, 10):
            list_cnf.append([-x1 * 10 - k, -x2 * 10 - k])

# input
matrix = [[0] * 9 for i in range(9)]  # 全初始化为0
for i in range(9):
    for j in range(9):
        c = line_n[9 * i + j]
        if c != '.':
            matrix[i][j] = int(c)
        else:
            matrix[i][j] = 0

# 已填入数字
for i in range(9):
    for j in range(9):
        k = matrix[i][j]
        if k != 0:
            list_cnf.append([100 * (i + 1) + 10 * (j + 1) + k])
