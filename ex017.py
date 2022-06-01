# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

# modo 01
import math

co = float(input('Informe o comprimento cateto oposto: '))
ca = float(input('informe o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa sera: {:.2f}'.format(hi))

# modo 02

from math import hypot

co = float(input('Informe o comprimento cateto oposto: '))
ca = float(input('informe o comprimento do cateto adjacente: '))
hi = hypot(co,ca)
print('A hipotenusa sera: {:.2f}'.format(hi))

