# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import random
n=(random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
print(f'os valores sorteados foram:{n}')
print(f'o maior valor sorteado foi :{max(n)} e o menor valor sorteado foi :{min(n)}')

