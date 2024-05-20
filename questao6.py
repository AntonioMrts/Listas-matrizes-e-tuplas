'''
Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o lançou n
vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de cada face.
'''

n = int(input("Digite o número de lançamentos do dado: "))

resultados = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
ocorrencias = [0, 0, 0, 0, 0, 0]

for resultado in resultados[:n]:
    ocorrencias[resultado - 1] += 1

for face in range(len(ocorrencias)):
    print(f"Face {face+1}: {ocorrencias[face]} ocorrencia(s).")
