#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas

distancia = int(input('Quantos km você percorreu? '))
calculo1 = (distancia*0.50)
calculo2 = (distancia*0.45)
if distancia <= 200:
    print(f'Você percorreu {distancia}km e por isso deverá pagar R${calculo1:.2f}!')
elif distancia > 200:
    print(f'Você percorreu {distancia}km e por isso deverá pagar R${calculo2:.2f}!')
