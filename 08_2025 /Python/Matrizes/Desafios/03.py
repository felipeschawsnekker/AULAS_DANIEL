# ==================================================
# VERIFICAR TODOS OS 8 QUADRADOS MÁGICOS 3x3
# ==================================================

# Quadrado mágico base
base = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

# Lista para armazenar os 8 quadrados mágicos
quadrados = []

# 1. Quadrado base
quadrados.append(base)

# 2-4. Rotacionar 90° três vezes
rot = [
    [base[2][0], base[1][0], base[0][0]],
    [base[2][1], base[1][1], base[0][1]],
    [base[2][2], base[1][2], base[0][2]]
]
quadrados.append(rot)

# Rotacionar mais duas vezes
for _ in range(2):
    nova_rot = [
        [rot[2][0], rot[1][0], rot[0][0]],
        [rot[2][1], rot[1][1], rot[0][1]],
        [rot[2][2], rot[1][2], rot[0][2]]
    ]
    quadrados.append(nova_rot)
    rot = nova_rot

# 5. Espelhamento horizontal do quadrado base
espelhado = [linha[::-1] for linha in base]
quadrados.append(espelhado)

# 6-8. Rotacionar o espelhado 3 vezes
rot = [
    [espelhado[2][0], espelhado[1][0], espelhado[0][0]],
    [espelhado[2][1], espelhado[1][1], espelhado[0][1]],
    [espelhado[2][2], espelhado[1][2], espelhado[0][2]]
]
quadrados.append(rot)

for _ in range(2):
    nova_rot = [
        [rot[2][0], rot[1][0], rot[0][0]],
        [rot[2][1], rot[1][1], rot[0][1]],
        [rot[2][2], rot[1][2], rot[0][2]]
    ]
    quadrados.append(nova_rot)
    rot = nova_rot

# ==================================================
# VERIFICAR CADA QUADRADO
# ==================================================
for idx, matriz in enumerate(quadrados):
    print(f"\nQuadrado mágico #{idx+1}:")
    
    # Mostrar a matriz
    for l in matriz:
        print(l)
    
    # Criar lista para armazenar as somas
    y = [0]*8  # 0-2 colunas, 3-5 linhas, 6 diag principal, 7 diag secundaria
    x = 3

    # SOMA DAS COLUNAS
    for j in range(x):
        for i in range(x):
            y[j] += matriz[i][j]

    # SOMA DAS LINHAS
    for i in range(x):
        for j in range(x):
            y[i+3] += matriz[i][j]

    # SOMA DAS DIAGONAIS
    for i in range(x):
        y[6] += matriz[i][i]        # diagonal principal
        y[7] += matriz[i][x-1-i]    # diagonal secundária

    # VERIFICAÇÃO
    todos_iguais = True
    v = y[0]
    for valor in y:
        if valor != v:
            todos_iguais = False
            break

    if todos_iguais:
        print("Esta matriz é mágica!")
    else:
        print("Esta matriz NÃO é mágica!")
