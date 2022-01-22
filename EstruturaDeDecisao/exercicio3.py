'''3.Faça um Programa que verifique se uma letra digitada é "F" ou "M".
 Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

sexo = input('Informe o sexo: (M ou F) ')


if sexo.upper() == 'M':
    print('Masculino')
elif sexo == 'F':
    print('Feminino')
else:
    print('Sexo não definido.')