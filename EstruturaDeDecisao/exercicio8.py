'''
8.Faça um programa que pergunte o preço de três produtos e 
informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
'''

preco1 = float(input('Informe o preço do primeiro produto '))
preco2 = float(input('Informe o preço do segundo produto ' ))
preco3 = float(input('Informe o preço do terceiro produto ' ))

def mais_barato(preco1, preco2, preco3):
    barato = preco1

    if preco2 < barato:
        barato = preco2
    if preco3 < barato:
        barato = preco3
    return barato

print('O produto a ser comprado custa ', mais_barato(preco1, preco2, preco3))