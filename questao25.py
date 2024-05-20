'''
Escreva um programa que substitua todos os elementos de uma matriz por um valor especificado pelo
usuário.
'''

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = int(input("Por qual numero deseja substituir toda a matriz: "))

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz:
            matriz[i][j] = n

for elementos in matriz:
    print(elementos)
