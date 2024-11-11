import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Grafico de linhas (plot)
#x = np.array([1, 2, 3, 4])
#y = x * 2 #broadcasting (multiplicar os valores de um vetor por um escalar)
#y2 = x ** 2
#plt.plot(x, y, '*--r', x, y2, '.-y', linewidth='5', markersize=20)
#plt.show()

#Subplot
#x = np.array([1, 2, 3, 4])
#y = x * 2 #broadcasting (multiplicar os valores de um vetor por um escalar)
#plt.subplot(1, 2, 1)
#plt.plot(x, y, '*--r', linewidth='5', markersize=20)
#y2 = x ** 2
#plt.subplot(1, 2, 2)
#plt.plot(x, y2, '.-y', linewidth='5', markersize=20)
#plt.show()

#Scatter plot
dfPaises = pd.read_csv('paises.csv', delimiter=';')
print(dfPaises.columns)

dfPaises2 = dfPaises.nlargest(6, 'Area (sq. mi.)')
print(dfPaises2)

plt.scatter(dfPaises2['Country'], dfPaises2['Area (sq. mi.)'], s=dfPaises2['GDP ($ per capita)'] / 10)
plt.show()
