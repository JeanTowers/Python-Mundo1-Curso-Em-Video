# Faça um programa que leia algo pelo teclado
# e mostre  na tela o seu tipo primitivo
# e todas informações possíveis sobre ele.

a= input('Digite algo: ')
print('o tipo primitivo do qeu foi digitado é:', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Esta em maiúsculas? ', a.isupper())
print('Esta em minúsculas? ', a.islower())
print('Esta capitalizada? ', a.istitle())