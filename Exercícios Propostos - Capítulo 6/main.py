#Bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Questão 1
dfSpace = pd.read_csv('space.csv', delimiter=';')

dfEUA = dfSpace[dfSpace['Location'].str.contains('USA')]
dfChina = dfSpace[dfSpace['Location'].str.contains('China')]

contEUA = dfEUA['Company Name'].nunique()
contChina = dfChina['Company Name'].nunique()

plt.title('Quantidade de empresas espaciais')
plt.xlabel("Países")
plt.ylabel("Quantidade")
plt.bar(['EUA', 'China'], [contEUA, contChina])

plt.show()

#Questão 2
dfPaises = pd.read_csv('paises.csv', delimiter=';')

dfPaises = dfPaises[dfPaises['Region'].str.contains('NORTHERN AMERICA')]

plt.title('Taxa de natalidade e mortalidade dos países da América do Norte')
plt.plot(dfPaises['Country'], dfPaises['Birthrate'], 'sb--', label='Taxa de natalidade')
plt.plot(dfPaises['Country'], dfPaises['Deathrate'], 'or--', label='Taxa de mortalidade')

plt.legend()
plt.show()