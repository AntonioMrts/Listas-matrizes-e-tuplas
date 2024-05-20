'''
Desenvolva um programa que inverta uma tupla
'''

n = int(input("Quantidade de numeros que deseja adicionar: "))
tupla = []
inverter = []

for i in range(n):
    tupla.append(int(input("Digite os numeros: ")))

for i in range(len(tupla) - 1, -1, -1):
    inverter.append(tupla[i])
tupla_invertida = tuple(inverter)

print(f"Tupla invertida:\n{tupla_invertida}")
