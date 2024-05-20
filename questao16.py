'''
Escreva um programa que receba duas listas, uma com os valores das notas e outra com os pesos
correspondentes, e calcule a média ponderada.
'''
n = int(input("Quantidade de numeros para adicionar na lista: "))

valores_notas = []
pesos_correspondentes = []

for i in range(n):
    valores_notas.append(float(input("Digite o valor das notas: ")))

for i in range(n):
    pesos_correspondentes.append(int(input("Digite os pesos coreespondentes: ")))

soma = 0
pesos = 0

for i in range(len(valores_notas)):
    soma += valores_notas[i] * pesos_correspondentes[i]
    pesos += pesos_correspondentes[i]

media = soma / pesos
print(f"Soma: {soma}")
print(f"Media: {media}")
