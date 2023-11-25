#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
#biblioteca
import random
#variaves de controle
victorias=computador=player=0
#funçao do computador
#mensagem inicial
print('-='*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*20)
#variavel de repetição
while player >=0:
    computador=int(random.randint(0,10))
    player=int(input('digite um numero'))
    parouinpar=str(input('P/I:')).upper()
    r=(player+computador)%2
    #condicional para victoria do par do player
    if parouinpar == 'P':
        if r ==0:
            print(f'a soma dos valores é: {player+computador},um numero par,você venceu')
            victorias+=1
            print('vamos jogar novamente......')

    #condicional para derota do par do player
        else:
            print(f'o resultado dos numeros é: {player+computador},um numero inpar,você perdeu')
            break
     #condicional para victoria do impar do player
    if parouinpar == 'I':
        if r >0:
            print(f'a soma dos valores é: {player+computador},um numero inpar , você venceu')
            victorias+=1
            print('vamos jogar novamente......')
        #condicional para derota do impar do player
        else:
            print(f'a soma dos valores é: {player+computador}, um numero par , você perdeu')
            break
#game over do jogo
print(f'game over!você venceu {victorias} vezes')

