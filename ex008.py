# Escreva um programa  que leia  um valor em metros e o exiba convertido em centímetros e milímetros.

metros = int(input('Digite o valor em metros: '))
centrimetros = metros * 100
milimetros = metros * 1000

print('{} metros convertido em centimetros é {} cm'.format(metros, centrimetros))
print('{} metros convertido em milimetros é {} mm'.format(metros, milimetros))