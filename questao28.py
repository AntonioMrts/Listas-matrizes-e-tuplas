'''
Escreva um programa que ordene uma lista de números de forma que os elementos se alternem entre
o maior e o menor valor. Por exemplo, a lista [1, 3, 5, 7, 9, 2, 4, 6, 8] se tornaria [9, 1, 8, 2, 7, 3, 6, 4,
5].
'''

numeros = [1, 3, 5, 7, 9, 2, 4, 6, 8]

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] < numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

lista_alternada = []

for i in range(len(numeros) // 2):
    lista_alternada.append(numeros[i])
    lista_alternada.append(numeros[-(i + 1)])

if len(numeros) % 2 != 0:
    lista_alternada.append(numeros[len(lista_alternada) // 2])

print(lista_alternada)
