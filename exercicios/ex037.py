#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro: '))
print('''Escolha uma base para conversão: 
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f' {num} convertido para Binário é {bin(num)[2:]}')
elif opcao == 2:
    print(f' {num} convertido para Octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f' {num} convertido para Hexadecimal é {hex(num)[2:]}')
else:
    print('Opção invalida!')
