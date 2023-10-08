def diferenca_dividida(x, y):
    n = len(x)
    tabela = [[None] * n for _ in range(n)]

    # Preenche a primeira coluna da tabela com os valores y
    for i in range(n):
        tabela[i][0] = y[i]

    # Calcula as diferenças divididas
    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = (tabela[i+1][j-1] - tabela[i][j-1]) / (x[i+j] - x[i])

    return tabela

def estimar_valor_faltante(x, y, x_faltante):
    n = len(x)
    tabela = diferenca_dividida(x, y)
    estimativa = tabela[0][0]

    for i in range(1, n):
        termo = tabela[0][i]
        for j in range(i):
            termo *= (x_faltante - x[j])
        estimativa += termo

    return estimativa

# Dados fornecidos
meses = [1, 2, 3, 4, 6]  # Valores conhecidos de meses
estatura = [45, 48, 49, 52, 66]  # Valores conhecidos de estatura
perimetro = [33, 34, 37, 42, 44]  # Valores conhecidos de perímetro

# Estimar estatura aos 5 meses
x_faltante = 5  # Valor faltante de meses
estatura_estimada = estimar_valor_faltante(meses, estatura, x_faltante)

print(f"A estatura estimada aos {x_faltante} meses é {estatura_estimada} cm.")
