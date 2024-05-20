'''
Crie um programa que receba uma matriz como entrada e retorne uma lista com as médias de cada
coluna.
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

medias = [0] * c 

for j in range(c):
    soma = 0
    for i in range(l):
        soma += matriz[i][j]
    medias[j] = soma / l

print(f"Médias de cada coluna da matriz:\n{medias}")
