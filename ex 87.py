#Aprimore o desafio anterior, mostrando no final:
#valores pares digitados. 
#A) A soma de todos os valores pares 
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

#criando listas
matrix=[[0,0,0],[0,0,0],[0,0,0]]
spar=mai=scol=0
#laço de repetiçao de linhas
for l in range(0,3):
    #laço de repetiçao de colunas
    for c in range(0,3):
        matrix[l][c]=(int(input(f'digite um numero[{l}][{c}]')))
        #soma dos numeros pares
        if matrix[l][c] % 2 == 0:
              spar += matrix[l][c]
#soma dos valores da terceira coluna              
for l in range(0,3):
    scol += matrix[l][2]
#maior valor da segunda linha 
for c in range(0,3):
    if c==0:
        mai == matrix [1][c]
    elif matrix[1][c]>mai:
        mai= matrix[1][c]   
#print da matrix
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matrix[l][c]:^5}]',end=' ')        
    print() 
#print da soma dos numeros pares
print(f'a soma dos numeros pares é {spar}')
#print da soma dos valores da terceira coluna
print(f'a soma dos valores da terceira coluna é {scol}')
#print o maior valor da segunda linha 
print(f'o maior valor da segunda linha é :{mai}')
            
