import sys


def carregar_mapa(map_filename):
    var_map = {}
    try:
        with open(map_filename, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2:
                    var_num = int(parts[0])
                    var_name = parts[1]
                    var_map[var_num] = var_name
    except FileNotFoundError:
        print(f"Erro: Arquivo de mapa '{map_filename}' não encontrado.")
        sys.exit(1)
    return var_map


def interpretar_resultado(res_filename, map_filename, verbose=False):
    var_map = carregar_mapa(map_filename)

    try:
        with open(res_filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Erro: Arquivo de resultado '{res_filename}' não encontrado.")
        sys.exit(1)

    if not lines:
        print("Erro: Arquivo de resultado está vazio.")
        return

    status = lines[0].strip()
    if status != "SAT":
        print(f"Resultado do Solver: {status}")
        print("Não foi encontrada uma solução válida para o problema.")
        return

    print("=== SOLUÇÃO ENCONTRADA (SAT) ===")

    literais = []
    for line in lines[1:]:
        parts = line.strip().split()
        for p in parts:
            if p != '0':
                literais.append(int(p))

    variaveis_verdadeiras = []
    for lit in literais:
        if lit > 0 and lit in var_map:
            variaveis_verdadeiras.append(var_map[lit])

    plano_por_tempo = {}
    for var in variaveis_verdadeiras:
        parts = var.split('_')
        predicado = parts[0]

        if predicado in ['at', 'lev']:
            bloco = parts[1]
            pos_ou_lev = int(parts[2])
            tempo = int(parts[3])

            if tempo not in plano_por_tempo:
                plano_por_tempo[tempo] = []

            if predicado == 'at':
                plano_por_tempo[tempo].append(f"Bloco '{bloco}' na Posição {pos_ou_lev}")
            elif predicado == 'lev':
                plano_por_tempo[tempo].append(f"Bloco '{bloco}' no Nível {pos_ou_lev}")

    for t in sorted(plano_por_tempo.keys()):
        print(f"\n--- Instante de Tempo t = {t} ---")
        for estado in sorted(plano_por_tempo[t]):
            print(f"  * {estado}")


if __name__ == "__main__":
    res_file = "resultado1.txt"
    map_file = "trab01_blocos2SAT.map"
    verbose = "-verbose" in sys.argv

    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        res_file = sys.argv[1]

    interpretar_resultado(res_file, map_file, verbose)