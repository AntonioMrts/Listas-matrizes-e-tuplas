'''
 Crie um programa que receba uma lista de palavras e conte quantas vezes cada vogal aparece no total.
'''

palavras = input("Digite a lista de palavras separadas por espaço: ").split()

vogais = "aeiou"

for vogal in vogais:
    quantidade = 0
    for palavra in palavras:
        quantidade_vogal = palavra.count(vogal)
        quantidade += quantidade_vogal
    print(f"{vogal} --> {quantidade} vezes.")
