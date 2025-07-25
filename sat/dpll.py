# 将列表转换为字典
def clauses_to_dict(clauses: list[list[int]]) -> dict[int, list[list[int]]]:
    l2c_tbl = dict()
    for c in clauses:
        for l in c:
            if l not in l2c_tbl:
                l2c_tbl[l] = []
            l2c_tbl[l].append(c)
    return l2c_tbl


# 赋值
def assign(x: int, _clauses: list[list[int]]) -> list[list[int]]:
    new_clauses = []
    for c in _clauses:
        if x in c:
            continue  # 子句被满足
        new_clause = [l for l in c if l != -x]
        new_clauses.append(new_clause)
    return new_clauses


# 找到出现次数最多的文字
def find_literal(clauses: list[list[int]]) -> int:
    freq = {}
    for c in clauses:
        for lit in c:
            freq[lit] = freq.get(lit, 0) + 1
    return max(freq.items(), key=lambda x: x[1])[0] if freq else 0


# 打印结果
def print_solution(solution: list[int]):
    # 将解转换为字典 {变量: 赋值}
    assignment = {}
    for lit in solution:
        var = abs(lit)
        val = 1 if lit > 0 else 0
        assignment[var] = val

    # 按变量顺序打印
    sorted_vars = sorted(assignment.keys())
    result = " ".join(f"{var}:{assignment[var]}" for var in sorted_vars)
    print("Solution:", result)


# dpll函数
def dpll_reduce(cur_literals: list[int], cur_clauses: list[list[int]]) -> bool:
    # 通过单子句规则化简
    while any(len(c) == 1 for c in cur_clauses):
        single_literal_clauses = [c for c in cur_clauses if len(c) == 1]
        single_literal = single_literal_clauses[0][0]
        cur_literals.append(single_literal)
        cur_clauses = assign(single_literal, cur_clauses)

        if not cur_clauses:  # 所有子句被满足
            print_solution(cur_literals)
            return True
        if [] in cur_clauses:  # 存在空子句（矛盾）
            return False

    # 判断是否结束
    if not cur_clauses:
        print_solution(cur_literals)
        return True
    if [] in cur_clauses:
        return False

    # 寻找子句最少的文字
    next_ltl = find_literal(cur_clauses)

    # 赋值为true
    reduced_clauses_true = assign(next_ltl, cur_clauses)
    if dpll_reduce(cur_literals + [next_ltl], reduced_clauses_true):
        return True

    # 赋值为false
    reduced_clauses_false = assign(-next_ltl, cur_clauses)
    return dpll_reduce(cur_literals + [-next_ltl], reduced_clauses_false)
