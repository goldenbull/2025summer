import dpll

lines = open("problems/SAT测试备选算例/满足算例/M/bart17.shuffled-231.cnf", "rt").readlines()

clauses = []
for s in lines:
    if s[0] == "c":
        continue
    elif s[0] == "p":
        ss = s.strip().split(" ")
        literal_cnt = int(ss[2])
        clause_cnt = int(ss[3])
        print(literal_cnt, clause_cnt)
    else:
        ss = s.strip().split(" ")
        clause = [int(v) for v in ss[:-1]]
        clauses.append(clause)

result = dpll.dpll_reduce([], clauses)
print(result)

exit()
