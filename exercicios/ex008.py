#Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm
mt = float(input('Digite a metragem: '))
cm = mt*100
mm = mt*1000
dm = mt/100
km = mt/1000
print (f'{mt}mt equivale a {cm}cm,{mm}mm, {dm}dm e {km}km!')