'''
4.Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

nota1 = int(input('Informe a primeira nota:'))
nota2 = int(input('Informe a segunda nota:'))
nota3 = int(input('Informe a terceira nota:'))
nota4 = int(input('Informe a quarta nota:'))

def calcula_media(nota1, nota2, nota3, nota4): 
    return (nota1 + nota2 + nota3 + nota4)/4

print(calcula_media(nota1, nota2, nota3, nota4))
