###
# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
#variaveis
a='s'
soma=quant=media=maior=menor=0
#estrutura de repetiçao
while a == 's'.lower():
    b=int(input('digite um numero:'))
    a=str(input('voce quer cotinuar a digitar numeros?[s/n]:').lower().strip()[0])
    soma+=b
    quant+= 1
#estrutura condicional para achar o maior e o menor valor
    if quant == 1:
        maior=menor=b
    else:
        if b>maior:
            maior=b
        if b<menor:
            menor=b

#saida de dados
media=soma/quant
print('voce digitou {} e a media entre eles é {} maior numero: {}, e o menor: {}'.format(quant,media,maior,menor))
