import dpll

lines = open("problems/test.cnf", "rt").readlines()

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

for i in range(pow(2, literal_cnt)):
    result = 1
    x = [int(c) for c in format(i, f"0{literal_cnt}b")]
    for clause in clauses:
        clause_sum = 0
        for literal in clause:
            pos = abs(literal) - 1
            value = x[pos]
            if literal < 0:
                value = 1 - value
            clause_sum += value
        result *= clause_sum

        if result == 0:
            break

    if result != 0:
        print(x)
        for i in range(literal_cnt):
            if x[i] == 1:
                print(i + 1, end=" ")
        print()

print("end")
