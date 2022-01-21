'''
15.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
 sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 
•salário bruto. 
•quanto pagou ao INSS. 
•quanto pagou ao sindicato. 
•o salário líquido. 
•calcule os descontos e o salário líquido, conforme a tabela abaixo: 
+ Salário Bruto : R$ 
- IR (11%) : R$ 
- INSS (8%) : R$ 
- Sindicato ( 5%) : R$ 
= Salário Liquido : R$ 
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

valor_hora = float(input('Valor da hora: '))
quant_hora = int(input('Quantidade de horas trabalhadas: '))
def salario_bruto(valor_hora, quant_hora):
    return valor_hora * quant_hora

def desc_ir(salario_bruto):
    return salario_bruto * 0.11

def desc_inss(salario_bruto):
    return salario_bruto * 0.08

def desc_sind(salario_bruto):
    return salario_bruto * 0.05

def salario_liq(salario_bruto, desc_sind, desc_ir, desc_inss):
    return salario_bruto - desc_sind - desc_ir- desc_inss

print(f'Salário Bruto: R$', salario_bruto(valor_hora, quant_hora))
print(f'IR(11%): R$', desc_ir(salario_bruto(valor_hora, quant_hora)))
print(f'INNS (8%): R$', desc_inss(salario_bruto(valor_hora, quant_hora)))
print(f'Sindicate (5%) R$', desc_sind(salario_bruto(valor_hora, quant_hora)))
print('O salário líquido será de R$',salario_liq(salario_bruto(valor_hora, quant_hora), desc_sind(salario_bruto(valor_hora, quant_hora)),desc_ir(salario_bruto(valor_hora, quant_hora)), desc_inss(salario_bruto(valor_hora, quant_hora))))
