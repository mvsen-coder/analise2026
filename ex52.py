import pandas as pd
df = pd.read_csv('ClassicDisco.csv')
for coluna in df.columns:
    print("Coluna ", coluna)