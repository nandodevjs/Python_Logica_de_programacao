"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se o número é par ou ímpar.
Caso o usuário não digite um número inteirom informe que não é um número inteiro.
"""

number = input('Digite um número inteiro: ')


#if number.isdigit():
try:    
  number_int = int(number)
  par_impar = number_int % 2 == 0
  par_impar_str = 'Impar'

  if par_impar:
    par_impar_str = 'par' 
  
  print(f'O numéro {number_int} é {par_impar_str}')

#else:
except:
  print('Você não digitou um número inteiro')