#Faça um programa que leia nome e peso de várias pessoas,                                      guardando tudo em uma lista. No final, mostre:                                                                                    A) Quantas pessoas foram   cadastradas.                                                                               B) Uma listagem com as pessoas mais pesadas.                                                                                  
#C) Uma listagem com as pessoas mais leves.

#listas 
pesoas=list()
bc=list()
mai=men=0
#contador de pessoas 
cp=0
#estrutura de repetição
while True: 
    #inputs para a lista pessoas
    pesoas.append(input('Nome:'))
    cp+=1
    pesoas.append(float(input('Peso:')))
    #verificando maior e menor peso
    if len(bc)==0:
        mai=men=pesoas[1]
    else:
        if pesoas[1]> mai:
            mai=pesoas[1]
     
        if pesoas[1]< men:
            men=pesoas[1]
    
                  
    #colocando a lista pessoas na lista bc
    bc.append(pesoas[:])
    pesoas.clear()
    #condicional para sair do loop
    p=input('deja sair S/N:')
    if p in 'sS':
        break
print('='*40)
#mostre na tela o total de pessoas cadastradas

print(f'foram cadastrada o toral de {cp} pessoas')
print(f'o maior peso foi {mai}kg de',end=" ")
for p in bc:
    #condição para maior pesso
    if p[1] == mai:
        print(f'{[p[0]]}',end=' ') 
print()  
print(f'o menor peso foi {men}kg',end=' ')
for p in bc:
    #condição para menor pesso
    if p[1] == men:
        print(f'[{p[0]}]',end=' ')
print()
        

