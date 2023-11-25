#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez,para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

#variaveis de controle
n1=n2=int(0)
#estruturas de repetição
while n1 >= 0:
    n1=int(input('digite a tabuada que deseja'))
    print('='*40)
    #estrutura de desição para parada do codigo
    if n1 >= 0:
        for n2 in range(0,10):
            n2+=1
            print(f'{n1} x {n2}={n1*n2}')
    print("="*40)




