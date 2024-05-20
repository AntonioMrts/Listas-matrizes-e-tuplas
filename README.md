# Listas-matrizes-e-tuplas
Exercícios de listas, tuplas e matrizes.

1. Escreva um código onde o usuário vai digitar o lado1 e o lado2 do retângulo e imprima este retângulo
em formato de asteriscos
Exemplo1: lado1=2 e lado2=4
* * * *
* * * *
Exemplo2: lado1=3 e lado2 = 10
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *

l = int(input("Digite o lado1 da matriz: "))
c = int(input("Digite o lado2 da matriz: "))

matriz = []

for i in range(l):
    matriz.append('*' * c)
    
for linha in matriz:
    print(linha)
