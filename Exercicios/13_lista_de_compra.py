"""
Faça uma lista de compras.
O usuário deve conseguir inserir, apagar e listar valores da lista.
Trate erros como "inexistente" na lista.
"""
import os

lista_de_compras = []

while True:
    acao = input('Inserir[i], Deletar[d], listar[l]: ')

    if acao == 'i':
        os.system('cls') ## Se estiver executando no terminal do linux, utilize 'clear'
        inserir = input('Digite o ítem que deseja inserir: ')
        lista_de_compras.append(inserir)
        print(lista_de_compras)
    elif acao == 'l':
        print(f'lista_de_compras atual: {lista_de_compras}')

        for i, valor in enumerate(lista_de_compras):
            print(i, valor)

    elif acao == 'd':
        print(f'Qual ítem deseja deletar? {lista_de_compras}')
        deletar = input('EXCLUIR O ÍTEM: ')
        deletar.lower()
        lista_de_compras.remove(deletar)
    else:
        ...