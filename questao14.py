'''
Elementos Únicos: Crie um algoritmo que retorne uma lista com os elementos que aparecem em apenas
uma das duas listas passadas como argumento.
'''

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
elementos_unicos = []

for elementos in lista1:
    if elementos not in lista2:
        elementos_unicos.append(elementos)
        
for elementos in lista2:
    if elementos not in lista1:
        elementos_unicos.append(elementos)

print(f"Elementos únicos: {elementos_unicos}")
