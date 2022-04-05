#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite seu salário atual: R$'))
au1 = salario + (salario*0.1)
au2 = salario + (salario*0.15)
if salario > 1250:
    print(f'Seu salário terá um aumento de 10% e passará a ser R${au1:.2f}!')
else:
    print(f'Seu salário terá um aumento de 15% e passará a ser R${au2:.2f}')


