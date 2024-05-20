'''
Crie um programa que receba uma matriz como entrada e retorne duas listas, uma com a soma dos
elementos de cada linha e outra com a soma dos elementos de cada coluna.
'''

linhas = int(input("Digite o tamanho da linha da matriz: "))
colunas = int(input("Digite o tamanho da colunha da matriz: "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input(f"Digite os numeros para a posicao {i}, {j}: ")))
    matriz.append(linha)
for linha in matriz:
    print(linha)

soma_linhas = []
soma_colunas = [0] * colunas

for i in range(linhas):
    soma_linha = 0
    for j in range(colunas):
        soma_linha += matriz[i][j]
        soma_colunas[j] += matriz[i][j]
    soma_linhas.append(soma_linha)

print(f"Soma das linhas: {soma_linha}")
print(f"Soma das colunas: {soma_colunas}")
