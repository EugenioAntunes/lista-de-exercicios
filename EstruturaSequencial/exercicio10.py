'''
10.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''

temp = float(input('Informe a temperatura em Celcius que deseja converter para Fahrenheit: '))
def converte(temp):
    return (temp * 9 / 5) + 32

print(f'{temp}°Celcius é igual a {converte(temp)}°Fahrenheit') 