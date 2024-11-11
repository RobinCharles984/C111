import numpy as np

# Carregando dataset

ds = np.loadtxt('paises.csv', delimiter=';',
                dtype='str', encoding='utf-8')

#Questão 1
print('Paises:', ds[:, 0])         # Nesse caso mostra todos os elementos e sem repeticao

print('Regiao:', ds[:, 1])# 'len' para ver a length

print('Populacao:', ds[:, 2])

print('Area:', ds[:, 3])

#Questão 2
print('Quantidade de Regiões:', len(np.unique(ds[:, 1])))
print('Regiões:', np.unique(ds[:, 1]))

#Questão 3
print('Taxa de alfabetização média:', np.mean(ds[1:, 9].astype(float)))

#Questão 4
cond = np.sum(ds[1:, 1] == 'NORTHERN AMERICA                   ')
print("Quantidade de Paises na America do Norte: ", cond)

#Questão 5
cond = np.maximum(ds[1:, 8] == 'LATIN AMER. & CARIB    ')
print("Maior renda per capita", cond)
