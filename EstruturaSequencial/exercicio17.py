import math
'''
17.Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. 
•Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: 
•comprar apenas latas de 18 litros; 
•comprar apenas galões de 3,6 litros; 
•misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, 
isto é, considere latas cheias.
'''

import re


area = float(input('Informe o tamanho da área a ser pintada: '))

def lata(area):
    return (area / 6) / 18

preco_lata = lata(area) * 80.0
print(f'Serão necessárias {math.ceil(lata(area))}latas para pintar')
print(f'Será gasta uma quantia de R${math.ceil(preco_lata)}')

def galao(area):
    return (area / 6) / 3.6

preco_galao= lata(area) * 25
print(f'Serão necessárias {math.ceil(galao(area))}latas para pintar')
print(f'Será gasta uma quantia de R${math.ceil(preco_galao)}')


