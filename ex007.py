# Desenvolva um programa  que leia as duas notas de um aluno, calcule e mostre sua média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media =  (nota1 + nota2) / 2
print('A media de {} e {} é {}'.format(nota1, nota2, media))
