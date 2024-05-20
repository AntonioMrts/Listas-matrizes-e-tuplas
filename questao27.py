'''
Desenvolva um programa que calcule a soma dos elementos das diagonais principal e secundária de
uma matriz.
'''

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_principal = 0
soma_secundaria = 0
tamanho = len(matriz)

for i in range(tamanho):
    soma_principal += matriz[i][i]
    soma_secundaria += matriz[i][tamanho - 1 - i]

print(f"Soma da diagonal principal: {soma_principal}")
print(f"Soma da diagonal secundaria: {soma_secundaria}")
