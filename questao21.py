'''
Crie um programa que receba uma tupla de números e retorne duas tuplas, uma contendo os números
pares e outra os números ímpares.
'''

n = int(input("Quantos numeros deseja adicionar: "))
receber_tupla = []
tupla1 = []
tupla2 = []

for i in range(n):
    numeros = int(input("Digite os numeros: "))
    receber_tupla.append(numeros)
tupla = tuple(receber_tupla)

for numeros in tupla:
    if numeros % 2 == 0:
        tupla1.append(numeros)
tupla_par = tuple(tupla1)

for numeros in tupla:
    if numeros % 2 != 0:
        tupla2.append(numeros)
tupla_impar = tuple(tupla2)

print(f"Tupla com números pares:\n{tupla_par}\n\nTupla com numeros impares:\n{tupla_impar}")
