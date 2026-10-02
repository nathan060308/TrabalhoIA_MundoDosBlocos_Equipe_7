import sys

BLOCKS = {'a': 1, 'b': 1, 'c': 2, 'd': 3}
BLOCK_LIST = list(BLOCKS.keys())

MAX_POINT = 6
SLOTS = [i for i in range(MAX_POINT)]

MAX_LEVEL = 3

HORIZON = 5

INIT_POS = {'c': 0, 'a': 3, 'b': 5, 'd': 3}
INIT_LEV = {'c': 0, 'a': 0, 'b': 0, 'd': 1}

GOAL_POS = {'c': 0, 'a': 2, 'd': 2, 'b': 5}
GOAL_LEV = {'c': 0, 'a': 1, 'd': 0, 'b': 0}

var_counter = 1
var_map = {}
inv_var_map = {}


def get_var(name):
    global var_counter, var_map, inv_var_map
    if name not in var_map:
        var_map[name] = var_counter
        inv_var_map[var_counter] = name
        var_counter += 1
    return var_map[name]


clauses = []


def add_clause(clause):
    clauses.append(clause)


print("Gerando modelo de SAT...")


def get_slots(p, length):
    return [p + i for i in range(length)]


def is_stable(b, p, lev):
    if lev == 0:
        return True
    req_slots = (BLOCKS[b] + 1) // 2
    return True


for t in range(HORIZON + 1):
    for b in BLOCK_LIST:
        l_b = BLOCKS[b]
        valid_positions = [p for p in range(MAX_POINT - l_b + 1)]

        add_clause([get_var(f"at_{b}_{p}_{t}") for p in valid_positions])
        for i in range(len(valid_positions)):
            for j in range(i + 1, len(valid_positions)):
                p1, p2 = valid_positions[i], valid_positions[j]
                add_clause([-get_var(f"at_{b}_{p1}_{t}"), -get_var(f"at_{b}_{p2}_{t}")])

        add_clause([get_var(f"lev_{b}_{l}_{t}") for l in range(MAX_LEVEL)])
        for l1 in range(MAX_LEVEL):
            for l2 in range(l1 + 1, MAX_LEVEL):
                add_clause([-get_var(f"lev_{b}_{l1}_{t}"), -get_var(f"lev_{b}_{l2}_{t}")])

    for l in range(MAX_LEVEL):
        for s in SLOTS:
            blocks_covering_s = []
            for b in BLOCK_LIST:
                l_b = BLOCKS[b]
                for p in range(MAX_POINT - l_b + 1):
                    if s in get_slots(p, l_b):
                        blocks_covering_s.append((b, p))

            for i in range(len(blocks_covering_s)):
                for j in range(i + 1, len(blocks_covering_s)):
                    b1, p1 = blocks_covering_s[i]
                    b2, p2 = blocks_covering_s[j]
                    if b1 != b2:
                        clause = [
                            -get_var(f"at_{b1}_{p1}_{t}"),
                            -get_var(f"lev_{b1}_{l}_{t}"),
                            -get_var(f"at_{b2}_{p2}_{t}"),
                            -get_var(f"lev_{b2}_{l}_{t}")
                        ]
                        add_clause(clause)

for b in BLOCK_LIST:
    add_clause([get_var(f"at_{b}_{INIT_POS[b]}_0")])
    add_clause([get_var(f"lev_{b}_{INIT_LEV[b]}_0")])

for b in GOAL_POS:
    add_clause([get_var(f"at_{b}_{GOAL_POS[b]}_{HORIZON}")])
for b in GOAL_LEV:
    add_clause([get_var(f"lev_{b}_{GOAL_LEV[b]}_{HORIZON}")])

cnf_filename = "trab01_blocos2SAT.cnf"
map_filename = "trab01_blocos2SAT.map"

with open(cnf_filename, "w") as f_cnf:
    f_cnf.write(f"c Arquivo CNF gerado para o Mundo dos Blocos\n")
    f_cnf.write(f"p cnf {var_counter - 1} {len(clauses)}\n")
    for clause in clauses:
        f_cnf.write(" ".join(map(str, clause)) + " 0\n")

with open(map_filename, "w") as f_map:
    for var_num, var_name in inv_var_map.items():
        f_map.write(f"{var_num} {var_name}\n")

print(f"Sucesso! Arquivos gerados:")
print(f" -> CNF: {cnf_filename} ({len(clauses)} cláusulas, {var_counter - 1} variáveis)")
print(f" -> MAP: {map_filename}")