'''
7.Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))
num3 = int(input('Informe outro número: '))

lista = [num1, num2, num3]

menor_valor = min(lista)
print(lista)
print(f'O menor valor da lista é {menor_valor}')
