# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor do produto: '))

desconto = preco * 0.95

print('O produto com desconto ficara: {:.2f}'.format(desconto))