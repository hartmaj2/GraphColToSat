from pysat.formula import CNF
from pysat.solvers import Solver


# create a satisfiable CNF formula "(-x1 ∨ x2) ∧ (-x1 ∨ -x2)":
cnf = CNF(from_clauses=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21],[-1,-4],[-2,-5],[-3,-6],[-4,-7],[-5,-8],[-6,-9],[-7,-10],[-8,-11],[-9,-12],[-7,-13],[-8,-14],[-9,-15],[-7,-16],[-8,-17],[-9,-18],[-13,-16],[-14,-17],[-15,-18],[-16,-19],[-17,-20],[-18,-21]])

# create a SAT solver for this formula:
with Solver(bootstrap_with=cnf) as solver:
    # 1.1 call the solver for this formula:
    print('formula is', f'{"s" if solver.solve() else "uns"}atisfiable')

    # 1.2 the formula is satisfiable and so has a model:
    print('and the model is:', solver.get_model())
