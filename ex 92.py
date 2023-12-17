#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
ano_atual=date.today().year
#dicionarios
empregado={}
empregado['nome']=str(input('nome:'))
empregado['data de nascimento']=int(input('data de nascimento:'))
empregado['idade']=ano_atual-empregado['data de nascimento']
empregado['Carteira De Trabalho']=int(input('carteira de trabalho(0 se não tem):'))


if empregado['Carteira De Trabalho']!=0:
    empregado['ano de contratação']=int(input('ano de contratação:'))
    empregado['salario']=float(input('salario:R$ '))
    empregado['aposentadoria']=empregado['ano de contratação']+35-empregado['data de nascimento']
    print('-='*25)

for n,i in empregado.items():
    print(f'- {n} tem o valor:{i}')



