# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salario do funcionario:'))

aumento = salario + (salario * 0.15)

print('O salário do funcionario e de {:.2f} reais, com aumento ficara: {:.2f} reais'.format(salario,aumento))

