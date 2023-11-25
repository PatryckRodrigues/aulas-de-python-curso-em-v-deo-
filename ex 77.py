#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
nomes='carne','frango','peru','hamburger','batata frita','suco'
for p in nomes:
    print(f'\nna palavra {p} temos',end=' ')
    for nomes in p:
        if nomes.lower() in 'aeiou':
            print(nomes,end=' ')
        