#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
v=list()
while True:
    n = int(input('digite um numero '))
    if n not in v:
        v.append(n)
    else:
        print('valor duplicado,não irei adicionar')
    e=str(input('deseja adicionar outro valor'))
    if e in ('N,n'):
       break
print(50*'=1')
print(f'os valores digitados foram:{v}')
    