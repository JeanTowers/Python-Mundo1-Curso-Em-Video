# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

preco = float(input('Informe o preço da compra: '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] em até 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
pagamento = int(input('qual a opção escolhida? '))

if pagamento == 1:

    final = preco - (preco * 0.10)
    print('O preço final da sua compra será de R${:.2f}'.format(final))

elif pagamento == 2:

    final = preco - (preco * 0.05)
    print('O preço final da sua compra será de R${:.2f}'.format(final))

elif pagamento == 3:
    final = preco
    parcela = preco/2
    print('Sua parcela ficara 2 vezes de {:.2f} SEM JUROS'.format(parcela))
elif pagamento == 4:
    final = preco + (preco * 0.20)
    parcela = int(input('Informe quantas parcelas deseja: '))
    vparcela = final / parcela
    print('Sua compra de R${:.2f} tera juros de 20% e ficara no valor Total de R${:.2f}, com o valor de cada parcela de R${:.2f}'.format(
        preco, final, vparcela))
else:
    print('Opção Incorreta')
