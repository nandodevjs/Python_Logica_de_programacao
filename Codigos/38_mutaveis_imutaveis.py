"""
(Imutável) - copiado o valor
(mutável) - aponta para o mesmo valor na memória
"""

listA = ['a','b','c']
#listB = listA
listB = listA.copy()

listA.insert(0, 'Fernando')

print(listA)
print(listB)