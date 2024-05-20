'''
Escreva um algoritmo que receba duas matrizes como entrada e retorne a soma dessas matrizes, desde
que tenham as mesmas dimensões.
'''

linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunhas: "))

matriz1 = []
print("Digite os elementos da primeira matriz:")

for i in range(linhas):
    linha = []
    for j in range(colunas):
        elemento = int(input(f"Digite o elemento da posicao {i}, {j}: "))
        linha.append(elemento)
    matriz1.append(linha)

print(matriz1)

matriz2 = []
print("Digite os elementos da segunda matriz:")

for i in range(linhas):
    linha = []
    for j in range(colunas):
        elemento = int(input(f"Digite o elemento da posicao {i}, {j}: "))
        linha.append(elemento)
    matriz2.append(linha)
    
print(matriz2)

if len(matriz1) != len(matriz2):
    print("As matrizes não possuem as mesmas dimensões.")
else:
    resultado = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(linha)

print(f"Soma das matrizes: {resultado}")
