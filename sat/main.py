import logging
import dpll

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.info("start")
    lines = open("problems/SAT测试备选算例/其它可供选择使用的算例/unif-k5-r21.117-v350-c7391-S5200354631670098160.cnf", "rt").readlines()

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

    for k, v in sorted(dpll.clauses_to_dict(clauses).items()):
        print(k, v)

    result = dpll.dpll_reduce([], clauses)
    print(result)
