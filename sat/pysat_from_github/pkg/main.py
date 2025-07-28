"""
SAT solver using CDCL
"""

import argparse
import os
from pkg.pysat import solver
from pkg.pysat import branch_heuristics as solvers
import logging

if __name__ == '__main__':
    FORMAT = '%(asctime)s.%(msecs)03d,%(levelname)s,%(process)d,%(filename)s:%(lineno)d,%(funcName)s,%(message)s'
    DATEFMT = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(level=logging.WARNING, format=FORMAT, datefmt=DATEFMT)

    parser = argparse.ArgumentParser(
        description='Reads a file and try to determine satisfiability by CDCL.'
                    ' Example usage: python3 -m pkg.main test/sample.cnf'
    )
    parser.add_argument(
        'filename',
        type=str,
        nargs='?',
        help='path of .cnf file')
    parser.add_argument(
        'heuristics',
        type=str,
        nargs='?',
        default='FrequentVarsFirstSolver',
        help='choose heuristics to branch variable'
             ': OrderedChoiceSolver '
             '| RandomChoiceSolver '
             '| FrequentVarsFirstSolver (default) '
             '| DynamicLargestIndividualSumSolver')
    parser.add_argument(
        '--loglevel',
        default='WARNING',
        nargs='?',
        help='level of logging (WARNING, DEBUG, etc.)')

    args = parser.parse_args()

    if args.filename is None:
        parser.print_help()
        exit()

    solver.logger.setLevel(args.loglevel)
    solver = getattr(solvers, args.heuristics)(args.filename)
    _, _, answer = solver.run()
    print(answer)
