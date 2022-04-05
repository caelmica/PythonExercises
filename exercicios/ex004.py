#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanuméro?', a.isalnum())
print('Está em maiusculas?', a.islower())
print('Está em minusculas?', a.isupper())
print('Está capitalizada?', a.istitle())




