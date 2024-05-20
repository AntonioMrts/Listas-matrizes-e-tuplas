'''
Diferença entre Listas: Escreva uma função que receba duas listas como entrada e retorne uma nova
lista contendo os elementos que estão presentes apenas em uma das listas, sem repetições.
Por exemplo:
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
A saída esperada seria:
[1, 2, 3, 6, 7, 8]
'''

lista1 = []
lista2 = []
nova_lista = []
n = int(input("Quantos numeros deseja colocar nas listas: "))

for i in range(n):
    lista1.append(int(input("Digite os numeros da primeira lista: ")))
for i in range(n):
    lista2.append(int(input("Digite os numeros da segunda lista: ")))

for elementos in lista1:
    if elementos not in lista2:
        nova_lista.append(elementos)
for elementos in lista2:
    if elementos not in lista1:
        nova_lista.append(elementos)

print(f"Elementos em apenas uma das listas:\n{nova_lista}")
