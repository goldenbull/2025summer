# 赋值：不再通过复制一个clauses并删除文字，而是创建一个空表往里添加文字
def assign(ltl:int,clauses:list[list[int]])->list[list[int]]:
    new_clauses = []
    for clause in clauses:
        if ltl in clause:
            continue  # 子句已满足
        new_clause = [l for l in clause if l != -ltl]
        if not new_clause:
            return None  # 发现空子句
        new_clauses.append(new_clause)
    return new_clauses

# 选择文字：选择出现频率最大的文字
def find_literal(clauses: list[list[int]]) -> int:
    freq = {}
    for c in clauses:
        for lit in c:
            freq[lit] = freq.get(lit, 0) + 1
    return max(freq.items(), key=lambda x: x[1])[0] if freq else 0

# dpll函数
def dpll_reduce(cur_literals: list[int], cur_clauses: list[list[int]]) -> list[int] or None:
    # 单子句策略
    changed=True
    while changed:
        changed=False
        single_clauses=[c for c in cur_clauses if len(c)==1]

        for c in single_clauses:
            single_ltl=c[0]
            if -single_ltl in cur_literals:
                return None
            if single_ltl not in cur_literals:
                cur_literals.append(single_ltl)
                cur_clauses=assign(single_ltl,cur_clauses)
                if cur_clauses is None:
                    return None
                changed=True

    #检查是否终止
    if not cur_clauses:
        return cur_literals
    if any(not c for c in cur_clauses):
        return None

    # 安全变量选择
    ltl = find_literal(cur_clauses)
    if ltl == 0:  # 新增关键检查
        return None

    #选择文字赋值
    ltl=find_literal(cur_clauses)

    #尝试赋值为True
    new_clauses=assign(ltl,cur_clauses)
    cur_literals=cur_literals+[ltl]
    result= dpll_reduce(cur_literals,new_clauses)
    if result is not None:
        return result

    #尝试赋值为False
    new_clauses=assign(-ltl,cur_clauses)
    cur_literals = cur_literals + [-ltl]
    result = dpll_reduce(cur_literals, new_clauses)
    return result