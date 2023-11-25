#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.

#variavei de controle
pessoa=idade=homens=mulheres=maioridade=sexo=0
while pessoa >=0:
    idade=int(input('idade:'))
    sexo=str(input('sexo: [m,f]')).upper()
    opcao=str(input('você deseja continuar?[s/n]')).upper()
    #maoires de 18 anos
    if idade >18:
        maioridade+=1
    #quantidades de homens
    if sexo == 'M':
        homens+=1
    #total de mulheres com menos de 20 anos
    if sexo=='F':
        if idade <20:
            mulheres+=1
    #opção de saida
    if opcao =='N':
        break
#saida de dados
print(f'total de pessoas com 18 anos ou mais:{maioridade}\ntotal de homens cadastrados:{homens}\no numero de mulheres com menos de 20 anos é :{mulheres}')
