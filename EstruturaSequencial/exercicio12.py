'''
12.Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 
'''

altura = float(input('Informe sua altura: '))
def peso_ideal(altura):
    return (72.7 * altura) - 58

print('Seu peso ideal é ', peso_ideal(altura))