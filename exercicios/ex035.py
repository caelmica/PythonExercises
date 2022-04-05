#Desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))
if c < a+b and b < a+c and a < b+c:
    print('\033[2;32;40mDá\033[m para formar um triângulo!')
else:
    print('\033[2;31;40mNão dá\033[m para formar um triângulo!')
