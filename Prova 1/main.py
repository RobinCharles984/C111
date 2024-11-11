# imports
import numpy as np

# recebendo o dataset
ds = np.loadtxt(fname='brands.csv', delimiter=';', dtype='str', encoding='utf-8')

# questao 1
valor2021 = ds[3:4, 10].astype(float)
valor2022 = ds[3:4, 9].astype(float)
valor21pra22 = valor2022 - valor2021

print('Valor em 2021: ', valor2021)
print('Valor em 2022:', valor2022)
print('Valorizou de 2021 para 2022: ', valor21pra22)

# questao 2
cont =  np.sum(ds[1:, 0] == 'Group')
print('Marcas o Group em seu nome: ', cont)

# questao 3
print('5 primeiras empresas: ', ds[1:6, 0], '. Valores de cada em 2023 com 10% de aumento: ', ds[1:6, 9].astype(float) + (ds[1:6, 9].astype(float) * 0.1))

# questao 4
slice1 = ds[1:, 0]
slice2 = ds[1:, 1]
slice3 = ds[1:, 2]

print('Nome da Empresa: ', slice1)
print('Quem fundou: ', slice2)
print('Quando fundou: ', slice3)

# questao 5
print('Anos em que se abriram empresas: ', np.unique(ds[1:, 2]))