'''
14.João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas. 
'''

peso = float(input('Informe o peso: '))
if peso < 50:
    print('Não houve exesso de peso.')
else:
    def exesso(peso):
        return peso - 50

    def multa(exesso):
        return  exesso * 4.00   


    print(f'Exesso de peso de {exesso(peso)}kg. Tera que pagar R${multa(exesso(peso))} de multa ')    
    