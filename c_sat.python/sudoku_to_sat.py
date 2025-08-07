from create_sudoku import *


def create_cnf(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    n = 0
    line_n = lines[n]
    list_cnf = []

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

    fout = open("my_sudoku.cnf", "wt")
    fout.write("c sudoku output\n")
    fout.write(f"p cnf {len(literals)} {len(clauses)}\n")
    for clause in clauses:
        for l in clause:
            print(l, end=' ', file=fout)
        print(0, file=fout)

    fout.close()
