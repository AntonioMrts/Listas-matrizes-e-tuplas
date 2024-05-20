'''2) Escreva um código similar à questão anterior, porém agora a figura deve ser vazia:
Exemplo2: lado1=3 e lado2 = 10
* * * * * * * * * *
*                 *
* * * * * * * * * *
'''

l = int(input("Digite o tamanho da linha da matriz: "))
c = int(input("Digite o tamanho da coluna da matriz: "))

matriz = [
    ['*' for _ in range(c)]
    for _ in range(l)
]

for i in range(1, l - 1):
    for j in range(1, c - 1):
        matriz[i][j] = " "
        
for linha in matriz:
    print(linha)
