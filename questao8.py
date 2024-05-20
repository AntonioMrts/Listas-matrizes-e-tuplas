'''
Escreva um algoritmo que encontre e retorne o maior elemento em uma lista de números.
'''

n = int(input("Quantidade para adicionar na lista: "))

lista_numeros = []

for i in range(n):
    lista_numeros.append(int(input("Digite os numeros: ")))

print(lista_numeros)

maior = lista_numeros[0]

for num in lista_numeros:
    if num > maior:
        maior = num

print(f"Maior numero: {maior}")
