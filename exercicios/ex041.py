# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
print('-='*20)
print('CONFEDERAÇÃO NACIONAL DE ATLETAS')
print('-='*20)
from datetime import date
nasc = int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual-nasc
if idade <= 9:
    print(f'Você tem {idade} anos e está na categoria MIRIM!')
elif idade <= 14:
    print(f'Você tem {idade} anos e está categoria INFANTIL!')
elif idade <= 19:
    print(f'Você tem {idade} anos e está na categoria JUNIOR!')
elif idade <=25:
    print(f'Você tem {idade} anos e está na categoria SÊNIOR!')
else:
    print(f'Você tem {idade} anos e está na categoria MASTER!')
