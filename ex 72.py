#Exercício Python 72: 
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

#lista de 0 a 20
ln=('zero','um',
'dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze',
'quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
while True:
    numero=int(input('digite o numero de 0 a 20:'))
    if 0<= numero <= 20:
        break
        numero=int(input('digite um numero valido:'))
print(f'o numero {numero} por extenso fica {ln[numero]}')
    
    
