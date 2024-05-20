'''
Escreva um programa que verifique se uma matriz é esparsa, ou seja, se a maioria dos seus elementos
é zero.
'''

l = int(input("Tamanho da linha da matriz: "))
c = int(input("Tamanho da coluna da matriz: "))

matriz = []

for i in range(l):
    linha = []
    for j in range(c):
        linha.append(int(input(f"Digite os numeros para a posicao {i}, {j}: ")))
    matriz.append(linha)
print(matriz)

for i in range(len(matriz)):
    if matriz[i][j] == 0:
        print("A matriz é esparsa! A maioria dos elementos é zero.")
    else:
        print("A matriz não é esparsa.")
