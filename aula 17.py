#num=(2,5,9,1)
#num=[2,5,9,1]
#num[0]=4
#num.append(7)
#inserindo valor na posição desejada
#num.insert(2,0)
#remoção de um valo
#num.pop(0)
#o reverse irar inverter a seguencia da lista
#num.sort(reverse=True)
#print(num)
#if 5 in num:
    #num.remove(5)
    #print(num)
#else:
    #print('nao achei o numero 5')    
#função para saber a qunatidade de elmentos da lista 
#print(f'essa lista tem {len(num)} elementos')
#print em lop da lista
valores=[]
#lendo lista pelo teclado
for cont in range(0,5):
    valores.append(int(input('digite um valor:')))

#valores.append(1)
#valores.append(2)
#valores.append(3)
for c,v in enumerate(valores):
    print(f'na posição {c} encontrei o numero {}!')
print('fim da lista')   