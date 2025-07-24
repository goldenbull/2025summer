def clauses_to_dict(clauses: list[list[int]]) -> dict[int, list[list[int]]]:
    l2c_tbl = dict()
    for c in clauses:
        for l in c:
            if l not in l2c_tbl:
                l2c_tbl[l] = []
            l2c_tbl[l].append(c)
    return l2c_tbl


def assign(x: int, _clauses: list[list[int]]) -> list[list[int]]:
    clauses = [c.copy() for c in _clauses]
    for c in clauses[:]:
        if x in c:
            clauses.remove(c)
        elif -x in c:
            c.remove(-x)
        else:
            ...
    return clauses


def find_literal(clauses_dict: dict[int, list[list[int]]]) -> int:
    counters = sorted([(len(v), k) for k, v in clauses_dict.items()])
    return counters[0][1]

def print_solution(solution:list[int]):
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


def dpll_reduce(cur_literals: list[int], cur_clauses: list[list[int]]) -> bool:
    new_clauses = [c.copy() for c in cur_clauses]

    # 通过单子句规则化简
    while any(len(c) == 1 for c in new_clauses):
        single_literal_clauses = [c for c in new_clauses if len(c) == 1]
        single_literal = single_literal_clauses[0][0]
        new_clauses = assign(single_literal, new_clauses)
        cur_literals.append(single_literal)

        if not new_clauses:  # 所有子句被满足
            print_solution(cur_literals)
            return True
        if [] in new_clauses:  # 存在空子句（矛盾）
            return False

    # 判断是否结束
    if not new_clauses:
        print_solution(cur_literals)
        return True
    if [] in new_clauses:
        return False

    # 寻找子句最少的文字
    clauses_dict = clauses_to_dict(new_clauses)
    next_ltl = find_literal(clauses_dict)

    # 赋值为true
    reduced_clauses_true = assign(next_ltl, new_clauses)
    if dpll_reduce(cur_literals + [next_ltl], reduced_clauses_true):
        return True

    # 赋值为false
    reduced_clauses_false = assign(-next_ltl, new_clauses)
    return dpll_reduce(cur_literals + [-next_ltl], reduced_clauses_false)
