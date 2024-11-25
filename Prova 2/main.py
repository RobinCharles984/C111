#Bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Questão 1
dsCars = pd.read_csv('electric_cars.csv',delimiter=',')
max_fastCharge = dsCars['Fast_charge'].max() 
fastChargeCars = dsCars[dsCars['Fast_charge'] == fastestSpeed]
chargeResults = fastChargeCars[['Car_name','Car_name_link']]
print(chargeResults)

#Questão 2
dist = dsCars['Range'].mean()
print("Alcance médio = ", dist)

#Questão 3
teslaCars = dsCars[dsCars['Car_name'].str.contains('Tesla')]
price = teslaCars['Price.DE.'].min()
low = dsCars[dsCars['Price.DE.']==price]
res = low['Car_name']
print("Carro mais barato da tesla = ", res)

#Questão 4
fast = dsCars.loc[dsCars['Top_speed'].idxmax()] 
slow = dsCars.loc[dsCars['Top_speed'].idxmin()] 

nameFast = fast['Car_name'] 
nameSlow = slow['Car_name']

plt.title('Carro mais rápido e o mais lento') 
plt.bar(['Rápido', 'Lento'], [fast['Top_speed'], slow['Top_speed']]) 
plt.xticks(['Rápido', 'Lento'], [nameFast, nameSlow]) 
plt.ylabel('Velocidade')        
plt.show()

#Questão 5
carsBYD = dsCars.nlargest(4,'Top_speed')
plt.title('Capacidadde de bateria dos 4 carros mais velozes da BYD')
plt.scatter(carsBYD['Car_name'], carsBYD['Battery'], s=carsBYD['Battery'])
plt.xlabel("Nome")
plt.ylabel("Bateria")
plt.show()