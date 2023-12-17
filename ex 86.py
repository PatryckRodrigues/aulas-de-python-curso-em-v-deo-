#criando listas
matrix=[[0,0,0],[0,0,0],[0,0,0]]
#laço de repetiçao de linhas
for l in range(0,3):
    #laço de repetiçao de colunas
    for c in range(0,3):
        matrix[l][c]=(int(input(f'digite um numero[{l}][{c}]')))
#print da matrix
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matrix[l][c]:^5}]',end=' ')        
    print()