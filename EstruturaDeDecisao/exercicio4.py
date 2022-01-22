'''
4.Faça um Programa que verifique se uma letra digitada 
é vogal ou consoante.
'''

letra = input("Digite qualquer letra: ")

lista = ['a','e','i','o','u']

if letra.upper() in lista:
    print(f'{letra} é uma vogal!')
else:
    print(f'{letra} é uma consoante!')