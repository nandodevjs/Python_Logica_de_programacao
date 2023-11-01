"""
Listas em Python
Tipo list é mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indice e fatiamento
Métodos úteis: apped, insert, pop, del, clear, extend, +

"""

string = "ABCDE" #5 caracteres
lista = list() # Posso utilizar para converter algum outro time em lista
lista = [123, True, 'Fernando', 1.2, []]

print(bool(lista)) # Uma lista vazia é False
print(lista, type(lista))

print(lista[2].upper(), type(lista[3]))

lista[2] = "Marques"

print(lista[2])