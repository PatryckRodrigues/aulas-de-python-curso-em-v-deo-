#test=[]
#.append('patryck')
#test.append(40)
#galera=[['joão',32],['lucas',34],['patryck',25]]
#o '[:]'serve para fazer uma copia de cada 
#galera.append(test[:])
#test[0]='maria'
#test[1]=22
#galera.append(test[:])
#for p in galera:
    #print(p)
    
#capturando dados pelo teclado 

galera=list()
dado=list()
menor=maior=0
for c in range(0,3):
    dado.append(str(input('nome:')))
    dado.append(int(input('idade:')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade')
        maior+=1
    else:
        print(f'{p[0]} é menor de idade')
        menor+=1    
print(f'temos {maior} pessoas maior de idade e {menor} pessoas menor de idade')        

