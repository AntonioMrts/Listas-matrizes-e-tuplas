'''
Lista Invertida: Crie um algoritmo que inverta uma lista de elementos.
'''

n = int(input("Quantidade para adicionar na lista: "))

lista = []

for i in range(n):
    lista.append(int(input("Digite os numeros: ")))

print(lista)

lista_invertida = []

for i in range(len(lista) - 1, -1, -1):
    lista_invertida.append(lista[i])
    
print(f"Lista invertida: {lista_invertida}")
