#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
#O programa será interrompido quando o número solicitado for negativo.


cont = 0
while True:
    num = int(input('Qual taboada você quer saber? [Negativo para parar] '))
    if num < 0:
        break
    print('*' * 20)
    print(f'TABOADA DO {num:^5}')
    print('*' * 20)
    for cont in range(0, 10):
        cont += 1
        produto = cont * num
        print(f'{cont} x {num} = {produto} ')
print('FIM DO PROGRAMA!')

