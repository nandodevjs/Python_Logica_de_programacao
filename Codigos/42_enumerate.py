"""
Enumerate = enumerar iteráveis (índices)

Enumerate numera cada indice da lista/tupla

enumerate(, start=19 )

"""

lista1 = ['Fernando', 'Marques', 'Silva']

#lista_enumerada = enumerate(lista1)

for i in list(enumerate(lista1, start=20)):
#    indice, nome = i
    print('For da tupla')
    for n in i:
        print(f'\t{n}')