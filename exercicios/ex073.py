#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
          'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo',
          'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print(f'Os 5 primeiros colocados são {tabela[0:5]}')
print(f'Os 4 últimos colocados são {tabela[16:21]}')
print(f'Ordem alfabética: {sorted(tabela)}')
print(f'A Chapecoense está em {tabela.index("Chapecoense")+1}° lugar.')