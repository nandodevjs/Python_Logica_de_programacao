'''
Operadores Lógicos
and (e)
or (ou)
not (não)

and = todas as condições precisam ser verdadeiras
Se qualquer expressão for considerado como falso, a expressão inteira será avaliada naquele valor.

São considerados falsos = 0, 0.0, '', Flase

Também existe o tipo None, que é usado para representar um não valor
'''

entrada = input('[E]ntrar [S]air ')
senha = input("Senha: ")

senha_permitida = "123456789"

if entrada == 'E' and senha == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avalização de curto circuito
print(True and False and True)