#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

#C) Quais foram os números pares.
valores = (int(input('digite o primeiro valor:')),
        int(input('digite o segundo valor:')),           
        int(input('digite o terceiro valor:')),            
        int(input('digite o ultimo valor:')))      
v9=valores.count(9)
print(f'o numero 9 aparece {v9} vezes ')
if 3 in valores:
    print(f'o numero 3 aparece pela primeira vez na {valores.index(3)}º posição')
else:
    print('o numero 3 não existe ')    
print('os valores pares são' ,end=' ')
for n in valores:
    if n % 2 == 0:
        print(n,end=' ')