#É possível criar os próprios dados e manipulá-los, sem precisar depender apenas do csv externo.
import pandas as pd 
dados = {
    'cargos': ["assistente", "analista", "gerente", "diretor"],
    'salario': [1000, 2000, 3000, 4000]
 }

dados_bi = pd.DataFrame(dados)
print(dados_bi)
#print(dados_bi.tail(1)) -> mostrar apenas a última linha
#print(dados_bi.head(1)) -> mostrar apenas a primeira linha
dados_bi.to_csv('salarios_cargos.csv', index=False, encoding='utf-8')
#utf-8 é para permitir acentuações
#index=False é para não incluir indexação
