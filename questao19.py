'''
Escreva um programa que ordene uma lista de números de forma que os números pares fiquem antes
dos números ímpares, mantendo a ordem original dentro de cada grupo.
'''

lista = [8, 9, 1, 4, 11, 6, 23, 2, 10, 12 ]

lista_parimpar = []

for pares in lista:
    if pares % 2 == 0:
        lista_parimpar.append(pares)

for impares in lista:
    if impares % 2 != 0:
        lista_parimpar.append(impares)

print(f"Lista com pares antes dos impares:\n{lista_parimpar}")
