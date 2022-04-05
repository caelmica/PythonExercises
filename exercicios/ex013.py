# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salario = float(input('Qual é seu salário? R$'))
novosal = salario +(salario*15/100)
print(f'Seu novo salário com aumento de 15% passa a ser R${novosal:.2f}')