"""
Round é usado para imprimir números decimais precisamente.
Decimal é uma bibliotéca para tratar dados em decimaios mais precisamente.
"""
import decimal


a = decimal.Decimal('0.1')
b = decimal.Decimal('0.7')
c = a + b

print(c)
print(type(round(c, 2)))
print(type(f'{c:.3f}'))
# Tomar cuidado com o type