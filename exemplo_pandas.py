import pandas as pd 

dados = pd.read_csv('portadosfundos.csv')
print(dados)

dados['views'] = [info.replace('views', 'visualizações') for info in dados['views']]
print(dados)
