#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos km você rodou? '))
dia = int(input('Quantos dias você rodou? '))
preco = (km*0.15)+(dia*60)
print(f'Por ter rodado {km}km e durante {dia} dias, você deve pagar R${preco} pelo aluguel do carro.')