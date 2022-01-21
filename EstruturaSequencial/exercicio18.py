'''
18.Faça um programa que peça o tamanho de um arquivo para download (em MB) e 
a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

tamanho = float(input('Informe o tamanho do arquivo:'))
velocidade = float(input('Informe a Velocidade de sua internet: '))

def tempo(tamanho, velocidade):
    return(tamanho/velocidade) / 60

print(f'Para baixar um arquivo de {tamanho}MB a uma velocidade de {velocidade}Mbps levará {tempo(tamanho, velocidade)}minutos')
