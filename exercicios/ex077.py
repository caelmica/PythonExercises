#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Manteiga', 'Pao', 'Tapioca', 'Cafe', 'Acucar', 'Faca')
for palavra in palavras:
    print(f'\nNa palavra {palavra} há as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
