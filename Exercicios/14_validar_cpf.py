"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  051.425.061-54
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

import re

cpf_client = input("CPF")
cpf_client = re.sub(
    r'[^0-9]',
    '',
    cpf_client
)

contador_regressivo = 10
resultado_1 = 0

nove_digitos = cpf_client[:9]

for i in nove_digitos:
    resultado_1 += int(i) * contador_regressivo
    contador_regressivo -= 1

digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)


############################################################
contador_regressivo_2 = 11
dez_digitos = nove_digitos + str(digito_1)

resultado_2 = 0

for i in dez_digitos:
    resultado_2 += int(i) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)

############################################
"""Validando CPF"""

novo_cpf = nove_digitos+str(digito_1)+str(digito_2)

if cpf_client == novo_cpf:
    print("Validado")
else:
    print("Não Validado")