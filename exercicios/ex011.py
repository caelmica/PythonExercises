# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e
# quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta pinta uma area de 2m2
largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
areap = largura*altura
print(f'Você precisa de {areap/2} litros de tinta para pintar a parede!')
