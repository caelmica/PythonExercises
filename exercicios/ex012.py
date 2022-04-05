#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input('Qual é o preço do produto? '))
desconto = preco*0.05
pdesconto = preco-desconto
print(f'O preço do produto com 5% de desconto é {pdesconto:.2f}')
