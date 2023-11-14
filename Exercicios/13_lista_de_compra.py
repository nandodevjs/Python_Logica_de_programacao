"""
Faça uma lista de compras.
O usuário deve conseguir inserir, apagar e listar valores da lista.
Trate erros como "inexistente" na lista.
"""

lista_de_compras = ['Arroz', 'Feijão', 'Fraudinha', 'Frango', 'Acém', 'Tomate', 'Alface']

acao = input('Inserir[i], Deletar[d], listar[l]: ')
valor = input([])

if acao == 'i':
    print(input(lista_de_compras.append(valor)))
elif acao == 'd':
    ...
elif acao == 'l':
    ...