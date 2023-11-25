#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

#variaveis de controle 
v=[]
#variaveis de repetição
for c in range(0,5):
    v.append(int(input('digite um numero')))
#maior valor da lista
maior=max(v)
#menor valor da lista
menor=min(v)
#o comando index indentifica a posiçao dentro das variaveis 
posição1=v.index(maior)
posição2=v.index(menor)
#saida de dados 
print(f'o maior numero é :{maior} na posiçao:1{posição1} e o valor minimo é:{menor} na posiçao:{posição2}')


 
    