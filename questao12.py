'''
Desenvolva um algoritmo que remova os elementos duplicados de uma lista e retorne uma nova lista
sem duplicatas.
'''

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

lista_sem_duplicatas = []

for elementos in lista1:
    if elementos not in lista2:
        lista_sem_duplicatas.append(elementos)

for elementos in lista2:
    if elementos not in lista1:
        lista_sem_duplicatas.append(elementos)
        
print(lista1)
print(lista2)
print(lista_sem_duplicatas)
