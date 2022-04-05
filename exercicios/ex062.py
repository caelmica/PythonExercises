#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += razao
        cont +=1
    print('PAUSA')
    mais = int(input('Quer mostrar mais quantos termos? '))
    print(f'{termo} → ', end='')
print(f'Progressão finalizada com {total} termos.')
