import math

'''
16.Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

import re


area = float(input('Digite o tamanho da área a ser pintado: '))

def qt_tinta(area):
    return math.ceil(area/3)


valor =math.ceil(qt_tinta(area)) * 80.00

print('Para pinta esta área precisará de ',qt_tinta(area), 'latas de tinta')
print('Para pinta esta área se gastará R$',valor)