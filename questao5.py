'''
Dada uma sequência de n números, imprimi-la na ordem inversa à da leitura.
'''

n = int(input("Digite a sequencia de números: "))

lista = []
lista_inversa = []

for i in range(n):
    lista.append(int(input("Digite os numeros: ")))

for i in range(len(lista) - 1, -1 , -1):
    lista_inversa.append(lista[i])
    
print(lista_inversa)
