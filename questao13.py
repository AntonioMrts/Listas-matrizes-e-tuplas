'''
Ordenação: Escreva um programa que ordene uma lista de números em ordem crescente ou
decrescente, dependendo do argumento passado para a função.
'''

numeros = [9, 3, 7, 1, 5]
ordem = input("Por favor, escolha crescente ou decrescente para a ordenação: ").lower()

if ordem == 'crescente':
    for i in range(len(numeros)):
        for j in range(0, len(numeros)-i-1):
            if numeros[j] > numeros[j+1]:
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
elif ordem == 'decrescente':
    for i in range(len(numeros)):
        for j in range(0, len(numeros)-i-1):
            if numeros[j] < numeros[j+1]:
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
else:
    print("Opçao inválida.")

print(f"Lista ordenada em ordem {ordem}: {numeros}")
