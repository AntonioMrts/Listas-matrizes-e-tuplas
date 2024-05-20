'''
Escreva um código que imprima uma matriz 5x5 com as duas diagonais com números 1 e o restante
da matriz com 0, exceto pelo número central que deve ser 3.
'''

matriz = [
    [0 for _ in range(5)]
    for _ in range(5)
]

for i in range(5):
    for j in range(5):
        if i == j or i + j == 4:
            matriz[i][j] = 1

matriz[2][2] = 3

for linha in matriz:
    print(linha)
