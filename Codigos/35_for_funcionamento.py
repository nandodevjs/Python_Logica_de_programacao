"""
Iterável -> STR, RANGE, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue o seu iterador
"""

# texto = iter('fernando') ## .__iter__()
# print(texto)
# print(next(texto))##.__next__()


texto = 'Fernando'
iterador = iter(texto)

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)