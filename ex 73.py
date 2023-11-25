#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol
# na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.

#b) Os últimos 4 colocados.

#c) Times em ordem alfabética.

#d) Em que posição está o time da Chapecoense.

listatop20=('Palmeiras','Botafogo','Grêmio','Bragantino','Atlético-MG','Flamengo','Athletico-PR','Fluminense','Cuiabá',
'São Paulo','Corinthians','Fortaleza','Internacional','Santos','Vasco','Cruzeiro','Bahia','Goiás','Coritiba','América-MG'
)
print(f'os 5 primeros colocados são:{listatop20[0:5]}\nos ultimos colocados sao{listatop20[15:20]}\nos times em ordem alfabeticam fica:{sorted(listatop20)}')
print(f'o time Internacional  esta na {listatop20.index('Internacional')+1}ºposiçao')

