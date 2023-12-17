#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

#dicionario
cadastro={}
#lista
dados=[]
mi=[]
#contador de pessoas
np=0
#estrutura de repetição geral
while True:
    #somando a quantidade de pessoas
    np+=1
    #cadastrando nome e sexo
    cadastro['nome']=str(input('nome:'))
    cadastro['sexo']=str(input('sexo: [M/F]'))
    #mensagem de erro casso o usuario digite uma opçao invalida
    if cadastro['sexo'] not in 'MmFf':
        print("ERRO! Por favor, digite apenas M ou F.")
        cadastro['sexo']=str(input('sexo: [M/F]'))
    #cadastrando idade
    cadastro['idade']=int(input('Idade:'))
    i=cadastro['idade']
    #registrando dados na memoria
    dados.append(cadastro.copy())
    mi.append(i)
    #se resposta for não , o pograma sera interonpido
    c=str(input('Quer continuar? [S/N]'))
    # mensagem de erro para opção invalida 
    if c not in 'sSnN':
        print('ERRO! Responda apenas s ou n')
        c=str(input('Quer continuar? [S/N]'))
    if c in 'Nn':
        break
cadastro['media']=sum(mi)/np
#calculo da idade media 
me=cadastro['media']
#saida de dados
print(f'A) Ao todo temos {np} pessoas cadastradas.')
print(f'B) A média de idade é de {me:5.2f} anos.')
print(f'C) As mulheres cadastradas foram:',end=' ')
for p in dados:
    if p['sexo']in 'Ff':
        print(f'{p['nome']}',end=' ')    
print()        
print('D) Lista das pessoas acima da media:')    
for p in dados :
    if p['idade']>=me:
        print(f'    nome = {p["nome"]} sexo={p["sexo"]} idade={p["idade"]}')
            
