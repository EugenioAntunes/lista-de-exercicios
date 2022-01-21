'''
13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: 
•Para homens: (72.7*h) - 58 
•Para mulheres: (62.1*h) – 44.7 
'''

altura = float(input('Informe sua altura: '))
sexo = input('Infome o seu sexo: ')

if sexo == 'h':
    def peso_ideal(altura):
        return (72.7 * altura) - 58
elif sexo == 'm':
    def peso_ideal(altura):
        return (62.1 * altura) - 44.7


print('Seu peso ideal é ', peso_ideal(altura))