import pandas as pd
import numpy as np

#Questao 1
dfPaises = pd.read_csv("paises.csv", delimiter=";") #Carregando dados
print(dfPaises[dfPaises['Region'] == 'OCEANIA                            ']) #Mostrando quais paises pertencem a regiao oceania

count = (dfPaises['Region'] == 'OCEANIA                            ').sum() #Mostrando quantos paises pertencem a regiao oceania
print(count)

#Questao 2
print(np.mean(dfPaises[['Literacy (%)']])) #Media da taxa de alfabetizacao do planeta

#Questao 3
maxPopulation = dfPaises[dfPaises['Population'] == dfPaises['Population'].max()]
print(maxPopulation['Country'].values[0]) #Mostrando nome do pais com maior populacao
print(maxPopulation['Region'].values[0]) #Mostrando nome da regiao com maior populacao

#Questao 4
dfCoast = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]
dfCoast.to_csv('noCoast.csv', sep=';', header=False)