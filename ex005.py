# Faça um programa que leia um número Inteiro e mostre na tela seu sucessor e seu antecessor.

n = int(input('Digite um numero: '))
suc = n + 1
ant = n - 1
print('o sucessor de {} é {} enquanto seu antecessor é {}'.format(n, suc, ant))
