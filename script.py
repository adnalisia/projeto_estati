import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kurtosis
from scipy.stats import normaltest, probplot


# Ler o arquivo de texto
df = pd.read_csv('data_1.txt', sep='\t', header=None, names=['dados'])

# Calculando os quartis
quartis = df['dados'].quantile([0.25, 0.5, 0.75, 1])

# Calculando a curtose
curtose = kurtosis(df['dados'])



# Exibe o DataFrame
print(df)
# Calculando as medidas de dispersão
media = round(df['dados'].mean(), 5)
mediana = round(df['dados'].median(), 5)
moda = round(df['dados'].mode()[0], 5)
variancia = round(df['dados'].var(), 5)
desvio_padrao = round(df['dados'].std(), 5)


#Exibindo os resultados
print(f'Média: {media}')
print(f'Mediana: {mediana}')
print(f'Moda: {moda}')
print(f'Variância: {variancia}')
print(f'Desvio Padrão: {desvio_padrao}')
print("Quartis:")
print(quartis)
print("\nCurtose:")
print(curtose)

#histograma
df['dados'].plot(kind='hist', bins=20)
plt.show()



# Boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(df['dados'])
plt.title('')
plt.ylabel('Tempo em segundos')
plt.show()


# Teste de normalidade
statistic, p_value = normaltest(df['dados'])
alpha = 0.05
print(f'Testando normalidade: statistic={statistic}, p-value={p_value}')
if p_value < alpha:
    print("Os dados não são normalmente distribuídos")
else:
    print("Os dados são normalmente distribuídos")

# Gráfico Q-Q
plt.figure(figsize=(8, 6))
probplot(df['dados'], dist='norm', plot=plt)
plt.title('Q-Q plot dos Dados de Tempo de Execução')
plt.xlabel('Quartis teóricos')
plt.ylabel('Quartis dos dados')
plt.show()
