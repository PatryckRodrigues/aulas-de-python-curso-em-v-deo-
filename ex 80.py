#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção 
# (sem usar o sort()). No final, mostre a lista ordenada na tela.

#variavel de contagem
r=[ ]

for c in range(0,5):
   n=int(input('digite um numero'))
   if c == 0 or n > r[-1]:
        r.append(n)
        print(f'adicionado no final da lista')
   else:
        poss=0
        while poss < len(r):
            if n <= r[poss]:
                r.insert(poss,n)
                print(f'adicionado na posição {poss}')
                break
            poss+=1
    
print(f'os valores em ordem sao:{r}')