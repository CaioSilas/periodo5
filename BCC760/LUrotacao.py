'''
  Funcao para impressao de matrizes
'''
def imprimeMatriz(matriz, descricao):
  numLinhas=len(matriz)
  numColunas=len(matriz[0])

  print(descricao)
  for i in range(numLinhas):
    for j in range(numColunas):
      print("%.2f\t"%matriz[i][j], end="")
    print()
  print()

'''
Funcao para impressao do vetor resultado
'''
def imprimeVetorResultado(vetor, descricao=""):
  print("Metodo: ", descricao)
  
  print("\nSolucao do sistema: [", end="" )
  for v in vetor:
    print("%.4f" % v, end=" ")
  print("]")


'''
  Funcao auxiliar para criar as matrizes L e U
'''
def criaMatrizes(A):
  matrizL = []
  matrizU = []
  numLinhas = len(A)
  
  for i in range(numLinhas):
    matrizL.append([])
    matrizU.append([])
    for j in range(numLinhas):
      matrizL[i].append(0)
      matrizU[i].append(0)

      if i==j:
        matrizL[i][j]=1

      matrizU[i][j] = A[i][j]
  
  return matrizL, matrizU



'''
  Funcao auxiliar. Calcular a operacao elementar da matriz
'''
def  operacaoElementar(m, linhaAtualizar, linhaBase):
  nCol = len(linhaAtualizar)
  for i in range(nCol):
    linhaAtualizar[i]= linhaAtualizar[i]+m*linhaBase[i]


'''
  Funcao auxiliar. Coletar coluna de uma matriz
  
'''
def getColuna(M, idColuna): # Considerando sempre uma matriz quadrada
  vetor = []
  numLinhas= len(M)

  for i in range(numLinhas):
    vetor.append(M[i][idColuna])
  

  return vetor



'''
  Algoritmo de substituicoes retroativas
'''

def substituicoesRetroativas(U, d):
    x = []
    n = len(d)  # número de posições de d (que é igual ao valor de n)
    for i in range(n):
        x.append(0)

    # Início do algoritmo de substituições retroativas
    if U[n-1][n-1] != 0:  # Verifica se não é uma divisão por zero
        x[n-1] = d[n-1] / U[n-1][n-1]
    else:
        # Trate o caso de divisão por zero aqui
        # Por exemplo, lançar uma exceção ou retornar um valor especial
        pass

    for i in range((n-2), -1, -1):
        soma = 0
        for j in range((i+1), n):
            soma += U[i][j] * x[j]

        if U[i][i] != 0:  # Verifica se não é uma divisão por zero
            x[i] = (d[i] - soma) / U[i][i]
        else:
            # Trate o caso de divisão por zero aqui
            # Por exemplo, lançar uma exceção ou retornar um valor especial
            pass

    return x  # x possui o mesmo tamanho de d
    # Fim do algoritmo de substituições retroativas


'''
  Algoritmo de substituicoes sucessivas
'''

def substituicoesSucessivas(L,c):
  x=[]
  n=len(c) # numero de posicoes de c (que eh igual ao valor de n)
  
  for i in range(n):
    x.append(0)
  
  # Incicio do algoritmo de substituicoes sucessivas
  x[0] = c[0]/L[0][0]
  
  for i in range(1,n):
    soma=0
    for j in range(i):
      soma+=L[i][j]*x[j]
    
    x[i]=(c[i]-soma)/L[i][i]
  return x # x possui o mesmo tamanho de c
  # Fim do algoritmo de substituicoes sucessivas

'''
  Função para fazer a troca das linhas caso necessario
'''

def trocarLinhas(matriz, linha1, linha2):
    matriz[linha1], matriz[linha2] = matriz[linha2], matriz[linha1]


# def decompoe(A):
#     L, U = criaMatrizes(A)

#     numLinhas = len(A)
#     numColunas = len(A[0])

#     for j in range(numLinhas):
#         # Pivoteamento parcial
#         maxElemento = abs(U[j][j])
#         linhaPivo = j
#         for i in range(j+1, numLinhas):
#             if abs(U[i][j]) > maxElemento:
#                 maxElemento = abs(U[i][j])
#                 linhaPivo = i

#         if linhaPivo != j:
#             trocarLinhas(U, linhaPivo, j)
#             trocarLinhas(L, linhaPivo, j)

#         for i in range(j+1, numLinhas):
#             multiplicador = -(U[i][j] / U[j][j])
#             operacaoElementar(multiplicador, U[i], U[j])
#             L[i][j] = -multiplicador

#     # imprimeMatriz(L, "Matriz L após todos os cálculos")
#     # imprimeMatriz(U, "Matriz U após todos os cálculos")

#     return L, U

def decompoe(A):
    L, U = criaMatrizes(A)

    numLinhas = len(A)
    numColunas = len(A[0])

    for j in range(numLinhas):
        # Pivoteamento parcial
        maxElemento = abs(U[j][j])
        linhaPivo = j
        for i in range(j+1, numLinhas):
            if abs(U[i][j]) > maxElemento:
                maxElemento = abs(U[i][j])
                linhaPivo = i

        if linhaPivo != j:
            trocarLinhas(U, linhaPivo, j)
            trocarLinhas(L, linhaPivo, j)

        for i in range(j+1, numLinhas):
            multiplicador = -(U[i][j] / U[j][j])
            operacaoElementar(multiplicador, U[i], U[j])
            L[i][j] = -multiplicador

    # Calcula a matriz inversa
    matrizInversa = []
    for j in range(numLinhas):
        b = [0] * numLinhas
        b[j] = 1
        y = substituicoesSucessivas(L, b)
        x = substituicoesRetroativas(U, y)
        matrizInversa.append(x)

    return matrizInversa


def decomposicaoLU(A,B):
  L,U= decompoe(A)

  matrizX = []
  numLinhas = len(B)
  numColunas = len(B[0])
  
  for i in range(numLinhas):
    matrizX.append([])
    for j in range(numLinhas):
      matrizX[i].append(0)
   
  for j in range(numColunas):
    x=[]
    b = getColuna(B,j)

    # Resolver o sistema linear Ly=b utilizando substituicoes sucessivas
    y=substituicoesSucessivas(L,b)
    
    # print("Resultado parcial y=", y)

    # Resolver o sistema linear Ux=y utilizando substituicoes retroativas
    x=substituicoesRetroativas(U,y)

    for i in range(numLinhas):
      matrizX[i][j] = x[i]
    

  return matrizX



def imprimeMatrizInversa(matriz):
    numLinhas = len(matriz)
    numColunas = len(matriz[0])

    print("Matriz Inversa:")
    for i in range(numLinhas):
        for j in range(numColunas):
            print("%.4f\t" % matriz[i][j], end="")
        print()
    print()

# A MATRIZ PASSADA NO EXERCICIO TA DANDO ERRO DE DIVISAO POR 0, NAO SEI SE ELA ESTA ERRADA OU SE É A LOGICA DO CODIGO
# A = [[1, 2, 0, 2, 1, 3],
#      [5, 2, 2, 2, -1, -4],
#      [-5, 5, 3, 5, 1, 4],
#      [3, 0, -1, -2, 3, 2],
#      [-2, 3, 5, 3, -1, 0],
#      [-1, -2, 4, 5, 2, -5]]  # Matriz de entrada

A = [[3, 3, 1],
     [1, 3, 0],
     [0, 2, 3]]

matrizInversa = decompoe(A)

imprimeMatrizInversa(matrizInversa)