#####Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:                                                                                                                                                
# A) Quantos números foram digitados.                                                                                                                    
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.

#variaveis
l=[]
#input da lista 
while True:
    l.append(int(input('digite um valor')))
    #mensagem de escolha do usuario
    e=str(input('deseja digitar outro valor S/N:'))
    #contador de elementos
    r=e.upper()
    #estrutura de desiçao para o fim do programa
    if r == 'N':
        break
#ordenando lista e invertendo a ordem    
l.sort (reverse=True) 
#o numero 5 estar na lista 
print('=-'*40)
print(f'você digitou {len(l)} elementos\na lista em ordem em decresente fica:{l}')
if 5 in l:
    print('o numero 5 faz parte da lista')
else:
    print('o numero 5 não faz parte da lista')