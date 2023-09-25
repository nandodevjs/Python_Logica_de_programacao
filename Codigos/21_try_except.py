"""
try e except são usados em Python para lidar com exceções, enquanto if e else são usados para controle de fluxo condicional. Eles servem a propósitos diferentes, mas podem ser usados juntos em certos casos para controlar o fluxo do programa com base em exceções.

Aqui está uma explicação das diferenças entre eles:

try e except:
try é usado para envolver um bloco de código que pode gerar uma exceção.
except é usado para especificar como o código deve reagir quando uma exceção é lançada dentro do bloco try. Você pode especificar o tipo de exceção que deseja capturar ou usar except sem um tipo para capturar qualquer exceção.
O código dentro do bloco except será executado somente se uma exceção for lançada no bloco try.
"""

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print(f'Float, {numero_float}')
    print(f'O dobro de {numero_str} é: {numero_float}')
except:
    print('Isso não é um número')