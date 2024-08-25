#Entrando com dados
nome:str = input("Nome do aluno(a):")
nota:int = input("Nota do aluno(a):")

#Guardando no dicionário
boletin = {"Nome": nome, "Nota": int(nota), "Situação": 0}

#Verificando média
if boletin["Nota"] >= 60:
    boletin["Situação"] = "AP"
else:
    boletin["Situação"] = "RP"

print(boletin["Situação"])

#Mostrando conteúdo do dicionário:
print(boletin)

