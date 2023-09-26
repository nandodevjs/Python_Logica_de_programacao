# """
# Faça um programa que peça o primeiro nome do usuário.
# Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto";
# Se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
# Mais que 6 letras, escreva "Seu nome é grande"
# """

nome = input('Digite seu primeiro nome: ')

nome_tamanho = len(nome)

if nome_tamanho > 1:
    if nome_tamanho <= 4:
        print('Seu nome é curto')
    elif nome_tamanho <= 5 or nome_tamanho <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é grande')
else:
    print('Por favor, digite pelo menos uma letra')

