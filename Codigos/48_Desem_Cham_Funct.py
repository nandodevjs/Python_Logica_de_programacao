string = 'ABC'
tupla = (1,2,3,4,5)
lista = ['Fernando', 1,2,3,4,5,6,7, 'Marques', 'Silva']

f, *_, M, S = lista
print(f, M, S)

print(*string)
print(*tupla)
print(*lista)

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda',(0,10,20,30,40)]
]

print(*salas, sep='\n')