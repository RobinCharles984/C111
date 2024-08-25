#Criando e preenchendo lista
teams = ["Real Madrid", "Milan", "Bayern de Munique", "Boca Juniors", "Barcelona"]
print(teams)

#Mostrando os 3 primeiros colocados
teams2 = teams.copy()
del teams2[4]
del teams2[3]
print(teams2)

#Mostrando os 2 ultimos colocados
teams3 = teams.copy()
del teams3[2]
del teams3[1]
del teams3[0]
print(teams3)

#Mostrando os times em ordem alfabética
teams4 = teams.copy()
teams4.sort()
print(teams4)

#Mostrando posição do time Barcelona na tabela original
a = 0
for i in teams:
    a = a + 1
    if i == "Barcelona":
        print(a)
