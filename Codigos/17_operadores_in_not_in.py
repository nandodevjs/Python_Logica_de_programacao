'''
Operadores in e not in

Strings são ITERÁVEIS (Você consegue acesar cada item dentro dela)

0   1  2  3  4  5  6  7
F   e  r  n  a  n  d  o
-8,-7,-6,-5,-4,-3,-2,-1,

'''

nome = 'Fernando'

print(nome[0])
print(nome[-8])

print("nan" in nome)
print("fu" in nome)

print("---" * 10)

print("nan" not in nome)
print("fu" not in nome)


nome = input("Digite seu nome: ")
encontrar = input("O que deseja encontrar no seu nome? ")

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
