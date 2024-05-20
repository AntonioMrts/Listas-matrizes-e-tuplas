'''
Remover Elemento Específico: Escreva um algoritmo que remova todas as ocorrências de um
elemento específico de uma lista. Portanto, o usuário deverá digitar qual elemento ele gostaria de retirar
da lista, e o algoritmo deverá substituir cada ocorrência deste número por um asterisco “*”.
'''

n = int(input("Quantidade para adicionar na lista: "))

lista = []

for i in range(n):
    lista.append(int(input("Digite os numeros: ")))

elemento = int(input("Digite qual elemento deseja remover da lista: "))

for i in range(len(lista)):
    if lista[i] == elemento:
        lista[i] = "*"
    else:
        print("Esse elemento não existe na lista")
    
print(lista)
