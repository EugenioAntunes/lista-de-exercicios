'''
7.Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''

altura = float(input('Informe a altura: '))
largura = float(input('Informe a largura: '))
def area(altura, largura):
    return (altura * largura) * 2

print(area(altura, largura))