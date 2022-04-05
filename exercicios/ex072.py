#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. S
# eu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <=20:
        break
    print('Número inválido!')
print(f'O número informado por extenso é: {extenso[num]} ')