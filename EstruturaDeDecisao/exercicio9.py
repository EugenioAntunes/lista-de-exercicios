'''
9.Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))
num3 = int(input('Informe outro número: '))

lista = [num1, num2, num3]

lista.sort()
lista.reverse()
print (lista)
