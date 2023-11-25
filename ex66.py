#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

#varivael
n=s=c=0
#estrutura de repetição
while n != 999:
    n=int(input('digite um numero'))
    if n == 999:
        #flag de pausa
        break
    #soma dos valores
    s+=n
    c+=1
#saida de dados
print(f'voce digitou {c} numeros e a soma de todos os numeros e igual a: {s}')


