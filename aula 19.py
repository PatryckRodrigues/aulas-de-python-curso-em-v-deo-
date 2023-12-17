#declarção de dicionarios
#pessoas={'nome':'patryck','sexo':'masculino','idade':'25'}
#pessoas['nome']='leandro'
#print de indicies
#print(f'o {pessoas["nome"]} tem {pessoas['idade']}anos ')
#for k, v in pessoas.items():
    #print(f'{k}={v}')
    
#dicionario dentro de listas
estado=dict()
brasil=list()
for c in range(0,3):
    estado['uf']=str(input('unidade federativa:'))
    estado['sigla']=str(input('sigla:'))
    brasil.append(estado.copy())
print(brasil)
