import sys
from pysat.formula import CNF
from pysat.solvers import Solver

# Se você não informar o nome no terminal, o padrão será 'resultado1.txt'
nome_saida = sys.argv[1] if len(sys.argv) > 1 else 'resultado1.txt'

formula = CNF(from_file='trab01_blocos2SAT.cnf')

with Solver(name='g3', bootstrap_with=formula) as solver:
    if solver.solve():
        model = solver.get_model()
        with open(nome_saida, 'w') as f:
            f.write("SAT\n")
            f.write(" ".join(map(str, model)) + " 0\n")
        print(f"Sucesso! Modelo SAT encontrado e salvo em '{nome_saida}'")
    else:
        with open(nome_saida, 'w') as f:
            f.write("UNSAT\n")
        print(f"UNSAT: Não foi possível encontrar um plano e foi salvo em '{nome_saida}'")