# Crie um programa que leia quanto dinhero uma pessoa tem
# na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$3,27

real = float(input('Digite quantos de dinheiro tem na carteira: R$ '))
dolar = 3.27
conversao = real / dolar
print('Com R${:.2f} pode se comprar US${:.2f}'.format(real, conversao))