"""
Split transforma um objeto em uma lista
"""

frase = 'Eu amo, pão de queijo'
lista_crua = frase.split(',')

# É uma boa prática salvar o valor mutável em uma variável e se precisar alterar salvar em outra variável
lista = []

for i, frase in enumerate(lista_crua):
    lista.append(lista_crua[i].strip())

print(lista)