"""
Faça um programa que pergunte a hora ao usuário,
baseando-se no horário descrito, exiba a saudação apropriada.
Ex: bom dia 0-11, boa tarde 12-17 e boa noite 18-23
"""
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)
    
    if hora >= 0 and hora <= 11:
        print('Bom dia')

    elif hora >= 12 and hora <= 17:
        print('Boa tarde')

    elif hora >= 18 and hora <= 23:
        print('Boa noite')
except:
    print('Por favor, digite números inteiros!')