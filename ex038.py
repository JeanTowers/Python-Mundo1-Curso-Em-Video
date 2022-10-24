# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. 
# mostrando na tela uma mensagem:

n1 = int(input('Informe o primeiro número inteiro: '))
n2 = int(input('Informe o segundo número inteiro: '))
if n1 > n2:
    print('O número {} e maior!'.format(n1))
elif n2 > n1:
    print('O número {} e maior'.format(n2))
else:
    print('Os números são Iguais')