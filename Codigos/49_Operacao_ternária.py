"""
Operação ternária = condicional de uma linha
valor if condicao else outro valor 
"""

condicao = 1 == 2
variavel = 'valor' if condicao else 'outro valor'
print(variavel)

digito = 11
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)