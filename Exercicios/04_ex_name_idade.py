"""
Peça ao usuário o nome e idade do usuário

Se o nome e idade forem fornecidos, exiba:

    Seu nome é {Nome}
    Seu nome invertido é {Nome invertido}
    Seu nome contém {ou não contem} espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}

Se nada for fornecido como entrada, exiba:
    "Desculpe, você deixou campos vazios"
    
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {''.join(reversed(nome))}")
    posicao_espaco = nome.find(" ")
    if posicao_espaco != -1: #  O método find retorna a posição do primeiro caractere encontrado na string, ou retorna -1 se o caractere não for encontrado.
        print(f"Seu nome contém espaços")
    else:
        print("Seu nome não contém espaço")
    print(f"Seu nome contém {len(nome)} letras") 
    primeira_letra = nome[0]
    print(f"A primeira letra do seu nome é {primeira_letra}")
    ultima_letra = nome[-1]
    print(f"A última letra do seu nome é {ultima_letra}")
else:
    print("Desculpe, você deixou campos vazios.")
