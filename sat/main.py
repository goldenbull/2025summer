import logging
import dpll_1
import dpll
import time

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.info("start")
    # fname = "problems/SAT测试备选算例/满足算例/M/ec-mod2c-rand3bip-sat-250-2.shuffled-as.sat05-2534.cnf"
    fname = "e:/workspace/s.cnf"
    lines = open(fname, "rt").readlines()

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

    start_time = time.time()  # 记录开始时间
    result = dpll.dpll_reduce([], clauses)
    end_time = time.time()  # 记录结束时间
    elapsed = end_time - start_time  # 计算耗时
    # 输出结果和耗时
    if result is not None:
        print("满足解:", sorted(result, key=abs))
    else:
        print("无解")
    print(f"执行时间: {elapsed:.4f}秒")
