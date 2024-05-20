'''
3) Escreva um código que imprimirá uma matriz de um tamanho digitado pelo usuário.
Por exemplo tamanho = 5, a matriz será 5x5
• Esta matriz deve ser composta de números aleatórios entre 1 e 9
• Imprima a soma de todos os números
• Imprima a média dos números
'''

from random import randint

tam = int(input("Digite o tamanho que sera a matriz (linha/coluna): "))

matriz = [
    [randint(1, 9) for _ in range(tam)]
    for _ in range(tam)
]

for linha in matriz:
    print(linha)
    
soma = 0

for elementos in matriz:
    for numeros in elementos:
        soma += numeros

media = soma / (tam * tam)

print(f"Soma: {soma}")
print(f"Media: {media:.2f}")
    
