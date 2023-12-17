import os
import configparser

def create_copy(filename, config, number):
    with open(filename, 'r') as file:
        data = file.read()

    for key, value in config.items():
        data = data.replace('{{' + key + '}}', value)

    with open(f'{filename}_{number}', 'w') as file:
        file.write(data)

config = configparser.ConfigParser()
config.read('config.ini')

filename = input("Digite o nome do arquivo que deseja preencher: ")

if not os.path.exists(filename):
    print("Arquivo não encontrado")
else:
    for i in range(1, 16):
        create_copy(filename, config, i)