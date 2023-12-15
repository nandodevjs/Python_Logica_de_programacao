"""
Listas de lista e seus índices
"""

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda',(0,10,20,30,40)]
]

#print(sala[2][3][2])

for sala in salas:
    print(sala)
    for aluno in sala:
        print(aluno)