# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salario do funcionario:'))

aumento = salario + (salario * 0.15)

print('O salário do funcionario e de {} reais, com aumento ficara: {} reais'.format(salario,aumento))

