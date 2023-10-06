string = 'Fernando'

i = 0

while i < len(string):

    letra = string[i]
    print(letra)

    if letra == ' ':
        break

    i += 1

else:
    print('Não encontrei um espaço na string')