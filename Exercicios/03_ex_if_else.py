primeiro_valor = input('Digite um número: ')
segundo_valor = input('Digite outro número: ')

if primeiro_valor != int:
    print("Digite um número valido")
elif primeiro_valor > segundo_valor:
    print(f"{primeiro_valor} é maior que {segundo_valor}")
elif segundo_valor > primeiro_valor:
    print(f"{segundo_valor} é maior que {primeiro_valor}")
else:
    print("digite um numero: ")