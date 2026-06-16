import pandas as pd #pandas é uma biblioteca que tem comandos para análise de dados.
df = pd.read_csv('ClassicDisco.csv') #read_csv é um comando do pandas. Esse comando vai ler e apresentar o conteúdo do arquivo csv.
#print(df) -> imprime a tabela inteira
#print(df.columns) -> nome de todas a colunas
#print(df.shape) -> quantidade de linhas e colunas
#print(df.head) -> mostra apenas sd primeiras linhas
#print(df.head(3)) -> mostra apenas as 3 primeiras linhas
#print(df.tail(5)) -> mostra apenas as 5 últimas linhas