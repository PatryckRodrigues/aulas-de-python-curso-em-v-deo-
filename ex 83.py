#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

#variaveis
expreçao=str(input('digite uma expreção')) 
pilha=[]
#adicionando a lista
for simb in expreçao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')' :
        if len (pilha) > 0:
            pilha.pop(0)
        else:
            pilha.append(')')
            break
#verificando expreção        
if len(pilha) == 0 :
    print('voce digitou uma exprexão valida')  
else:
    print('voce digitou uma expreçao invalida')              
#revisar esse exercio posteriormente 