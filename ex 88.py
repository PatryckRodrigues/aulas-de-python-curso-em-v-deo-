#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
lista=[]
jogo=[]
print('$'*30)
print('      JOGA NA MEGASENA     ')
print('$'*30)
quantidade=int(input('digite quantos jogos deseja fazer:'))
tot=1
while tot <= quantidade:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >=6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    tot+=1
print(f'$$$$sorteando{quantidade}jogos$$$$$')
for i,l in enumerate(jogo):
    print(f'jogo{i}:{l}')