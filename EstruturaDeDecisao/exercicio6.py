'''
6.Faça um Programa que leia três números e mostre o maior deles.
'''

num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))
num3 = int(input('Informe outro número: '))

lista = [num1, num2, num3]

maior_valor = max(lista)
print(lista)
print(f'O maior valor na lista é {maior_valor}')

