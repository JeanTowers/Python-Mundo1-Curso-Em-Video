# Crie um programa que leia quanto dinhero uma pessoa tem
# na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$3,27

dinheiro = float(input('Digite quantos de dinheiro tem na carteira: '))
dolar = 3.27
conversao = dinheiro / dolar
print('Com R${} pode se comprar US${:.2}'.format(dinheiro, conversao))