'''
 Escreva um programa que receba uma tupla e conte quantos elementos únicos ela possui.
'''

n = int(input("Quantidade de numeros para adicionar na tupla: "))
receber_tupla = []
unicos = []

for i in range(n):
    receber_tupla.append(int(input("Digite os numeros: ")))
tupla = tuple(receber_tupla)

for elementos in tupla:
    if elementos not in unicos:
        unicos.append(elementos)
elementos_unicos = tuple(unicos)

print(f"Tupla possui {len(elementos_unicos)} elementos unicos.") 
