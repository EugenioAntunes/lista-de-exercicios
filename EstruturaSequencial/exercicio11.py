'''
11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 
•o produto do dobro do primeiro com metade do segundo . 
•a soma do triplo do primeiro com o terceiro. 
•o terceiro elevado ao cubo. 

'''

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = float(input('Informe o terceiro número: '))

def operacoes(num1, num2, num3):
    x = (num1 * 2) * (num2 / 2)
    y = (num1 * 3) + num3
    z = num3**3
    return (x, y, z)

print(operacoes(num1,num2,num3))
