#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
#importando biblioteca
import random
import time
from _operator import itemgetter
#lista de jogadores
jogador={}
cj=0
podio=0
for n in range(0,4):
    cj+=1
    jogador[f'jogador {cj}:']=random.randint(1,6)
ranking={}
print('jogando dados...........')
for k,v in jogador.items():
    time.sleep(5)
    print(f'o {k} jogou {v} no dado')
ranking=sorted(jogador.items(),key=itemgetter(1),reverse=True)
for c,v in ranking:
    podio+=1
    print(f'o {c} ficou em {podio}º lugar,jogando {v} no dado')
