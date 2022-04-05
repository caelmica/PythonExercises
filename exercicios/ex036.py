# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('-='*20)
print('ANÁLISE DE APROVAÇÃO DE EMPRÉSTIMOS')
print('-='*20)
casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos quer pagar? '))
prestacao = (casa/anos)/12
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}.')
import time
if prestacao >= salario*0.3:
    print('PROCESSANDO SOLICITAÇÃO...')
    time.sleep(3)
    print('EMPRÉSTIMO \33[2;31;43mNEGADO\33[m, você ultrapassou o limite de 30% de seu salário!')
else:
    print('PROCESSANDO SOLICITAÇÃO...')
    time.sleep(3)
    print('EMPRÉSTIMO \33[2;32;40mAPROVADO\33[m!')
