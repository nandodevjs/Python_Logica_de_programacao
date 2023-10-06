frase = 'O Python é uma linguagem de programação' \
        'Multiparadigma.' \
        'Python foi criado por Guido Van Rossum'

i = 0

while i < len(frase):

    letra_atual = frase[i]
    
    count_letras = frase.count(letra_atual)

    print(letra_atual,)