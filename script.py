import pandas as pd

# Ler o arquivo de texto
df = pd.read_csv('data_1.txt', sep='\t', header=None, names=['dados'])

# Exibe o DataFrame
print(df)
# Calculando as medidas de dispersão
media = round(df['dados'].mean(), 5)
variancia = round(df['dados'].var(), 5)
desvio_padrao = round(df['dados'].std(), 5)

#Exibindo os resultados
print(f'Média: {media}')
print(f'Variância: {variancia}')
print(f'Desvio Padrão: {desvio_padrao}')


