'''
Crie um algoritmo que receba uma lista de números e retorne a soma de todos os elementos.
'''

n = int(input("Quantidade para adicionar na lista: "))

lista_numeros = []

for i in range(n):
    lista_numeros.append(int(input("Digite os numeros: ")))

soma = 0

for elementos in lista_numeros:
    soma += elementos

print(f"A soma de todos os elementos é: {soma}")
