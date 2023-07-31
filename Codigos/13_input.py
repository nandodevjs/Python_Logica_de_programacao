usuario = input('Qual é o seu nome? ')

nascimento = int(input('Qual o ano em que você nasceu? '))
ano = int(input('Qual é o ano atual? '))

idade_total = ano - nascimento

print(f'Muito prazer {usuario=}, a sua idade é: {idade_total} anos') # O sinal de = é utilizado para também imprimir o nome da variável