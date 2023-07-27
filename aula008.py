# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e
# milímetros.
valor = float(input('Insira um valor em metros: '))
km = valor / 1000
cm = valor * 100
mm = valor * 1000
print(f'Convertendo em:\nkm:{km}\ncm:{cm}\nmm:{mm}')
