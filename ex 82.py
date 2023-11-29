#Crie um programa que vai ler vários números e colocar em uma lista. 
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
#Ao final, mostre o conteúdo das três listas geradas.
#variaveis

n=0
i=[]
p=[]
v=[]
#estrutura de repetição
while True:
    n=int(input('digite um numero:'))
    
    if n %2==0:
        p.append(n)
    else:
        i.append(n)
    o=input('deseja continuar s/n:').upper()
    v.append(n)
    if o == 'N':
    
        break
print(f'a lista conpleta é :{v}')
print(f'voce digitou os seguintes numeros pares{p}') 
print(f'voce digitou os seguintes numeros inpares{i}') 

    
