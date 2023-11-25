#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato
#variaveis de controle e acumulador
gt=quant=p=p1000=vp=0
barato=''
#estrutura de repetição
while p >=0:
    nome=input('digite o nome do produto:')
    p=int(input('digite o preço do produto:'))
    opcao=input('quer continuar [S/N]').upper()
    gt+=p
    quant+=1
    if p >1000:
        p1000+=1
    if quant == 1:
        vp=p
        barato=nome
    else:
        if p<vp:
            vp=p
            barato
    if opcao == 'N':
        break
#saida de dados     
print(f'o total gasto nas conpra é {gt}\ntemos {p1000} produto custando mais de 1000R$\no nome do produto mais barato é: {barato} , com valor de {vp}R$')
