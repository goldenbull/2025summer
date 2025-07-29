import logging
import dpll

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.info("start")
    # fname = "problems/SAT测试备选算例/满足算例/M/m-mod2c-rand3bip-sat-220-3.shuffled-as.sat05-2490-311.cnf"
    # fname = "problems/SAT测试备选算例/基准算例/功能测试/sat-20.cnf"
    # fname = "problems/SAT测试备选算例/满足算例/L/eh-vmpc_25.renamed-as.sat05-1913-625.cnf"
    # fname="problems/SAT测试备选算例/满足算例/S/problem2-50.cnf"
    fname = "/Users/cjn/Downloads/CBS_k3_n100_m403_b10/CBS_k3_n100_m403_b10_3.cnf"
    lines = open(fname, "rt").readlines()

    clauses = []
    for s in lines:
        if s[0] == "c":
            continue
        elif s[0] == "p":
            ss = s.strip().split()
            literal_cnt = int(ss[2])
            clause_cnt = int(ss[3])
            print(literal_cnt, clause_cnt)
        else:
            ss = s.strip().split()
            clause = [int(v) for v in ss[:-1]]
            clauses.append(clause)

    result = dpll.dpll_reduce([], clauses)
    print(result)
