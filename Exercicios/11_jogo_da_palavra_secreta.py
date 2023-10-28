import os


"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.

- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.  
- Faça a contagem de tentativas do seu usuário.
"""

palavra_secreta = 'pepino'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')

    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')    
        continue

    if letra_digitada == ' ':
        print('Não aceitamos espaço vazio!')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for i in palavra_secreta:
        if i in letras_acertadas:
            palavra_formada += i
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print(f'Parabéns! Você concluiu o jogo! A palavra secreta é: {palavra_secreta}',
              f'numero de tentativas: {numero_tentativas}')
        letras_acertadas = ''
        numero_tentativas = 0
        break
    
    os.system('clear')