import numpy as np
#
# # # SLICING DE DADOS
# np.random.seed(10)
# arr = np.random.randint(1,10,10)
# #arr2 = arr[0:4] # fazendo assim os arrays estão interligados para economizar memoria (mudando arr2, muda arr)
# arr2 = arr[0:4].copy()  #.copy impede isso de acontecer
# arr2[0] = 9
# arr2[1] = 9
# print(arr)
# print(arr2)


# CONDICIONAIS

# np.random.seed(10)
# arr = np.random.randint(1,10,10)
# print(arr)          #Vetor original
# print(arr < 5)      #Condicional - Cria uma máscara de True e False
# print(arr[arr < 5]) #Buscando elementos onde na máscara seja True

# print(arr)            #Vetor original
# cond = arr % 2 == 0   #Cria uma variavel para guardar o condicional (numero par)
# print(cond)           #Condicional - Cria uma máscara de True e False
# print(arr[cond])      #Buscando elementos onde na máscara seja True


# # ANALISE TEXTUAL (CHAR)
#
# arr = np.array(['Vinicius', 'Victor', 'Warley', 'Solange', 'Yasmin', 'Charles'])
# # FIND
# cond = np.char.find(arr,'Vi') >= 0 #CASE SENSITIVE (<0 nao encontrou // >=0 encontrou o padrao)
# print(cond)
# # CONDICIONAL
# print(arr[cond])


# CARREGANDO UM DATASET

ds = np.loadtxt('space.csv', delimiter=';',
                dtype='str', encoding='utf-8')            # Carrega o dataset
# print(ds)                                               # Mostra o dataset
print('Colunas: ', ds[0, :])                              # ':' para fazer um slicing que mostra TODAS as COLUNAS

# Quais as diferentes empresas deste dataset que ja realizaram missoes espaciais?

# print('Nome das Empresas:', ds[1:, 1])                  # Não consegue mostrar todos os elementos e mostra elementos repetidos
                                                          # '1:' para remover a primeira linha (que são as colunas)
print('Nome das Empresas:', np.unique(ds[:, 1]))          # Nesse caso mostra todos os elementos e sem repeticao

# Quantas diferentes empresas deste dataset que ja realizaram missoes espaciais?

print('Quantidade de Empresas:', len(np.unique(ds[:, 1])))# 'len' para ver a length