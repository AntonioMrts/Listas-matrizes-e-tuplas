'''
Desenvolva um programa que remova todos os elementos ímpares de uma lista e imprima a lista
resultante.
'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_resultante = []

for elementos in lista:
    if elementos % 2 == 0:
        lista_resultante.append(elementos)

print(f"Lista resultante: {lista_resultante}")
