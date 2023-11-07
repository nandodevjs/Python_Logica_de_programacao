"""
Listas em Python
Tipo list é mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indice e fatiamento
Métodos úteis: 
    apped = adiciona um indice no final da lista
    insert = adiciona um indice (posição, valor)
    pop = remove e retorna o indice
    del = deleta o indice
    clear = 
    extend =
Create Read update Deleted

"""

string = "ABCDE" #5 caracteres
lista = list() # Posso utilizar para converter algum outro time em lista
lista = [123, True, 'Fernando', 1.2, []]

print(bool(lista)) # Uma lista vazia é False
print(lista, type(lista))

print(lista[2].upper(), type(lista[3]))

lista[2] = "Marques"

print(lista[2])

del lista[4]

print(lista[3])

## Adicionando indices na lista

lista.append([10,20,30,40,[10,20]])
print(lista)

## Remove o último indice da lista

lista.pop() ## pop retorna o valor que foi removido.

print(lista)

del lista[-1] ## Remove o último indice da lista

########### DEL APAGA, POP REMOVE E RETORNA O VALOR DO ÍNDICE ###########

## Insert = possui dois parâmetros, a posição do indice e o valor á ser adicionado

lista.insert(0, 'Fernando')
print(lista)

listaB = ['Parker']
## Extend = retornará None, então não retorna nenhum valor, porém ele modifica o valor inicial ()

lista.extend(listaB)

print(lista)

###### Concatenando listas

listC = [1,2,3,4,5]
listD = [6,7,8,9,10]

listE = listC + listD
print(listE)