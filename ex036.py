# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#  Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#  A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Informe o valor da casa a ser financiada: '))
salario = float(input('Informe seu salario: '))
anos = int(input('Informme em quantos anos pretende pagar o emprestimo: '))

parcela = casa / (anos * 12)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação ficara no valor de R${:.2f}'.format(casa, anos, parcela))

if parcela >= (salario * 0.3):
    print('Emprestimo Negado!!!')

else:
    print('Emprestimo Aprovado!!!')
