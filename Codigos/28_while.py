"""

Em Python, o while é uma estrutura de controle de fluxo que permite que você execute um bloco de código repetidamente enquanto uma condição específica for verdadeira. O while é conhecido como um loop de controle de fluxo, pois ele cria um loop que continua executando enquanto a condição especificada for avaliada como verdadeira. Assim que a condição se tornar falsa, a execução do loop será interrompida, e o programa continuará a partir do ponto após o loop.

While = Enquanto

"""
condicao = True

while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')


####################################################

contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)

print('Acabou')