'''
6.Faça um Programa que peça o raio de um círculo, calcule e mostre sua área
'''

raio = float(input('Informe o valor do raio: '))
def calc_area(raio):
    return 3.14 * raio**2

print('A área do circulo é ', calc_area(raio))