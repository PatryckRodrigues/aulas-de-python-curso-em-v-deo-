#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
n=0
cp=0
#dicionarios
jogador={}
gp=[]
#declarações de dicionarios
jogador['nome:']=str(input('nome:'))
np= int(input(f'quantas partidas {jogador["nome:"]}jogou?'))
for c in range(1,np+1):
    gp.append(int(input(f'quantos gols voce fez na {c}º partida?')))
print('-='*30)
jogador['gols']=gp[:]
jogador['total']=sum(gp)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('-='*30)
print(f'o jogador {jogador["nome:"]} jogou {c} partidas.')
print('-='*30)
for i, v in enumerate(gp):
    print(f'      =>na partida {i+1} fez {v} gols')
print(f'foi um total de {jogador["total"]} gols')
    

