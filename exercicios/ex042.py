#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

l1 = float(input('Qual o tamanho do primeiro lado? '))
l2 = float(input('Qual o tamanho do segundo lado? '))
l3 = float(input('Qual o tamanho do terceiro lado? '))
if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    print('Pode formar um triângulo!')
    if l1 == l2 and l1 == l3:
        print('O triângulo formado é EQUILATERO!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('O triângulo formado é ISOSCELES!')
    else:
        print('O triângulo formado é ESCALENO!')
else:
    print('Não pode formar um triângulo!')
