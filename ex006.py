# Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um numero: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero **(1/2)

print('O dobro de {} é {}, seu triplo é {} e sua raiz é {:.3}'.format(numero, dobro, triplo, raiz))