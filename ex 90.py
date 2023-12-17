#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

#listas
aluno={}
aluno['nome']=str(input('nome:'))
aluno['media']=float(input('media:'))
if aluno['media'] >= 7:
    aluno['situação']='aprovado'
elif 5 <= aluno['media'] < 7:
    aluno["situação"]='recuperação'   
else:
    aluno['situação']='reprovado'
print('='*30)
for v,k in aluno.items():
    print(f'o {v} igual a {k}')
