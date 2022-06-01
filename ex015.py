# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Informe quantos Kilometos percorridos com o carro: '))
diasAlugado = float(input('Informe quantos dias o carro foi alugado: '))

pago = (km * 0.15) + (diasAlugado * 60)
print('O valor a ser pago pelo aluguel é de: R$ {:.2f}'. format(pago))


