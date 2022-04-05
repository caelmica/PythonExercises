#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
somapar = soma3 = 0
maior = list()
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}] [{c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]
        maior.append(matriz[1][c])
print('-'*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^8}]', end='')
    print()
print(f' A soma dos valores pares digitados é: {somapar}')
print(f' A soma dos valores da terceira coluna é: {soma3}')
print(f'O maior valor da segunda linha é{max(maior)}')



