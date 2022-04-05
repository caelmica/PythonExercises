#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
num = float(input('Digite um ângulo qualquer: '))
s = math.sin(math.radians(num))
c = math.cos(math.radians(num))
t = math.tan(math.radians(num))
print(f'Para o número {num} o valor de Seno é {s:.2f}, o valor do Cosseno é {c:.2f} e o valor da Tangente é {t:.2f}!')
