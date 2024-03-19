from tabulate import tabulate

import pandas as pd

# Leia o arquivo de texto
df = pd.read_csv('data_1.txt', sep='\t')

# Exiba o DataFrame
print(df)

