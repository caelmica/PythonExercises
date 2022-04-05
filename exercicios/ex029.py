# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('Em que velocidade você estava dirigindo? '))
multa = (velocidade-80)*7
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade e será multado!')
    if velocidade > 80:
        print(f'Você deve pagar: R${multa} de multa!')
else:
        print('Você está dentro do limite de velocidade, continue assim!')
