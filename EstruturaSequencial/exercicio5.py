'''
5.Faça um Programa que converta metros para centímetros. 
'''

medida = float(input('Informe a medida que deseja converter: '))
def conversor(medida):
    return medida*100

print(f'{medida} metro(s) após ser convertido tem {conversor(medida)} centimetros')