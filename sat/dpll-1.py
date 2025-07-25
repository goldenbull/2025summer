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

def dpll_reduce(cur_literals: list[int], cur_clauses: list[list[int]]) -> list[int] or None:
    # 单子句策略
    changed=True
    while changed:
        