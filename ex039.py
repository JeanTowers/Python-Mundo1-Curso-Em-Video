# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
#  de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#  se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('Informe seu sexo. M para masculino e F para feminino. ')
sexo =  input('Sua Opção: ')

if sexo == 'M':

    nasc = int(input('Informe seu ano de nascimento: '))

    atual = date.today().year

    idade = atual - nasc

    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

    if idade == 18:
        print('Você precisa se alistar esse Ano.')

    elif idade > 18:
        saldo = idade - 18
        alist = atual - saldo
        print('Você deveria ter se alistado há {} anos.'.format(saldo))
        print('Seu alistamento foi em {}.'.format(alist))

    elif idade < 18:
        saldo = 18 - idade
        alist = atual + saldo
        print('Faltam {} anos para seu alistamento.'.format(saldo))
        print('Seu alistamento sera em {}.'.format(alist))

elif sexo == 'F':
    print('Você não precisa se alistar, alistamento e obrigatorio apenas para o sexo masculino.')

else:
    print('Dados informado incorretamente!')