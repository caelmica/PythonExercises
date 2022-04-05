#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’
#Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = ''
while sexo != 'M' and sexo != 'F':
     sexo = input('Digite o sexo da pessoa [M/F]: ').upper().strip()[0]
     if sexo != 'M' and sexo != 'F':
        print('Você não digitou a opção correta, tente novamente!')
print(f'Você digitou corretamente, o sexo é {sexo}')
