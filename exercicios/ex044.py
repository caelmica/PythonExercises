#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

preco = float(input('Qual o valor do produto? R$'))
opcao = int(input('''Opção de pagamento:
[1] À vista dinheiro/cheque.
[2] À vista no cartão.
[3] 2x no cartão.
[4] 3x ou mais no cartão
Digite sua opção: '''))
if opcao == 1:
    print(f'À vista no dinheiro/cheque você pagará R${preco-(preco*0.1):.2f}!')
elif opcao == 2:
    print(f'À vista no cartão vcê pagará R${preco-(preco*0.05):.2f}')
elif opcao == 3:
    print(f'Em 2x no cartão você pagará R${preco:.2f}')
elif opcao == 4:
    print(f'Em 3x ou mais no cartão você pagará R${preco+(preco*0.2):.2f}')
else:
    print('Opção inválida!')
