#contador
numero=cont=soma=0
#soma
#estrutura de repetição
while numero !=999:
   numero=int(input('digite um numero'))
   if numero == 999:
      break
   soma+=numero
#saida de dados
#print("a soma vale{}"format(soma))
print(f'a soma vale:{soma}')
import pygame