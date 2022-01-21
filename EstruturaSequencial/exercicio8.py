'''
8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 
'''

valor_hora = float(input('Valor da hora: '))
qunt_hora = int(input('Quantidade de horas trabalhadas: '))
def salario(valor_hora, qunt_hora):
    return valor_hora * qunt_hora

print('O seu salário este mes será de ', salario(valor_hora, qunt_hora))