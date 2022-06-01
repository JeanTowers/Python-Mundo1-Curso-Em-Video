# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# modo 01
num = float(input('Informe um valor: '))
print('O valor informado foi {} e a sua porção inteira é {}'.format(num, int(num)))

# modo 02
from math import trunc

num = float(input('Informe um valor: '))
print('O valor informado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

