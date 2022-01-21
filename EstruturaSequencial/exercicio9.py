'''
9.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 
•C = 5 * ((F-32) / 9).
'''

temp = float(input('Informe a temperatura em Fahrenheit que deseja converter para Celcius: '))
def converte(temp):
    return (temp - 32) * 5 / 9

print(f'{temp}° Fahrenheit é igual a {converte(temp)}° Celsius') 