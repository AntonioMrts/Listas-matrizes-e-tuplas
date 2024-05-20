'''
Escreva um programa que receba duas tuplas como entrada e retorne uma nova tupla contendo todos
os elementos das duas tuplas, sem repetições
'''

tupla1 = tuple(input("Digite os elementos da primeira tupla separado por espaço: ").split())
tupla2 = tuple(input("Digite os elementos da segunda tupla separado por espaço: ").split())

nova_tupla = ()
for elemento in tupla1 + tupla2:
    if elemento not in nova_tupla:
        nova_tupla += (elemento,)

print(nova_tupla)
