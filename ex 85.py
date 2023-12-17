#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

#listas
numeros=[],[]
valores=0
#adicionando valores as listas
for p in range(1,8):
    valores=int(input(f'digite o {p}º valor:'))
    #condicinal para os numeros pares
    if valores%2==0:
        numeros[0].append(valores)
    #condicinal para os numeros inpares    
    else:
        numeros[1].append(valores)
#colocando os numeros em ordem crescente            
numeros[0].sort()
numeros[1].sort()  
#inprimindo numeros pares      
print(f'os numeros pares são:{numeros[0]}')
#inprimindo numeros inpares
print(f'os numeros inpares são:{numeros[1]}')        