# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Informe um numero inteiro: '))

print('Escolha umas das bases para conversão: ')
print('[ 1 ] converter para BINÀRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
escolhe = int(input('Sua opção: '))

if escolhe == 1:
    print('{} convertido em BINARIO é: {}'.format(n, bin(n)[2:]))
elif escolhe == 2:
    print('{} convertido em OCTAL é: {}'.format(n, oct(n)[2:]))
elif escolhe == 3:
    print('{} convertido em HEXADECIMAL é: {}'.format(n, hex(n)[2:]))
else:
    print('Opção Invalida')
