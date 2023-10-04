while True:

    number_1 = input("Digite um número: ")
    number_2 = input("Digite outro número: ")
    operador = input("Digite o operador: ('+', '-', '/' ou '*') ")

    number_1_float = 0
    number_2_float = 0

    numeros_validos = None

    try:
        number_1_float = float(number_1)
        number_2_float = float(number_2)
        numeros_validos = True
    except Exception as error:
        numeros_validos = None

    if numeros_validos is None:
        print(f'Um ou ambos os números digitados são inválidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador')


    if operador == "+":
        print(number_1_float + number_2_float)

    elif operador == "-":
        print(number_1_float - number_2_float)

    elif operador == "*":
        print(number_1_float * number_2_float)

    elif operador == "/":
        print(number_1_float / number_2_float)

    else:
        "Nunca deveria ter chegado aqui"

    sair = input('Quer sair? [n]ão [s]im: ').lower().startswith('s')
    
    if sair is True:
        break 