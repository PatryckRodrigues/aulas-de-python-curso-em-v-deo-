#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção 
# (sem usar o sort()). No final, mostre a lista ordenada na tela.

v=[]
for c in range(0,5):
    r=int(input('digite um numero'))
    if  v==0 or r > v[-1]:
        v.append(r)
    


      
for p,o in enumerate(r):
    print(f'o {o} estar na posiçao {p}')