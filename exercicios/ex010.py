#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre qts dolares ela pode comprar. Considere 3,27
d = float(input('Quantos reais você tem? '))
c = d/3.27
print('Você pode comprar {:.2f} dólares!'.format(c))