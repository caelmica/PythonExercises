from random import randint
numeros = list()
def sorteia():
    numeros.append(randint(0, 10))
    numeros.append(randint(0, 10))
    numeros.append(randint(0, 10))
    numeros.append(randint(0, 10))
    numeros.append(randint(0, 10))

def somapar():
    soma = 0
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            soma += v
    print(f'A soma dos valores pares da lista é {soma}')


sorteia()
print(numeros)
somapar()
