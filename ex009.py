# Faça um programa  que leia um número inteiro qualquer e mostre na tela sua tabuada.

numero = int(input('Digite o numero que deseja saber a tabuada: '))

for tabuada in range(10):

    resultado = numero * (tabuada+1)
    print('{} vezes {} = {}'.format(numero, tabuada+1, resultado))
