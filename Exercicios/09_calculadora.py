number_1 = input("Digite um número: ")
number_2 = input("Digite outro número: ")
operador = input("Digite o operador: ('+', '-', '/' ou '*')")

while True:
    sair = input('Quer sair? [n]ão [s]im').lower().startswith('s')
    
    if sair is True:
        break