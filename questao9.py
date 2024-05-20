'''
Média dos Elementos: Desenvolva um algoritmo que calcule e retorne a média dos elementos de uma
lista de números.
'''
n = int(input("Quantidade para adicionar na lista: "))

lista_numeros = []

for i in range(n):
    lista_numeros.append(float(input("Digite os numeros: ")))

print(lista_numeros)

soma = 0

for elementos in lista_numeros:
    soma += elementos

media = soma / n
    
print(f"Soma: {soma}")
print(f"Media: {media:.2f}")

