#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite a expressão: '))
contabr = expressao.count('(')
contfecha = expressao.count((')'))
somaparenteses = contfecha + contabr
if somaparenteses % 2 == 0:
    print(f' A Expressão "{expressao}" é válida!')
elif somaparenteses % 2 == 1:
    print(f'A Expressão "{expressao}" é inválida!')

