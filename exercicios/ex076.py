#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Sabão', 1.50, 'Detergente', 2.00, 'Pasta de Dente', 3.00, 'Desodorante', 5.00, 'Shampoo', 10)
print('-'*40)
print(f'{"TABELA DE PREÇOS":^40}')
print('-'*40)
for item in range (0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'R${lista[item]:>7.2f}')
