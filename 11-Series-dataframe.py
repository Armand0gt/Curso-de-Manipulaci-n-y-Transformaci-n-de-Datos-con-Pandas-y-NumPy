import pandas as pd

Jugadores = pd.Series(["Navas","Mbappe","Neymar","Messi"],
                 index=[1,7,10,30])
print(Jugadores)

Jugadores = pd.Series(["Navas","Mbappe","Neymar","Messi"])
print(Jugadores)

#Diccionario
diccionario = {1:"Navas", 7:"Mbappe",10:"Neymar",30:"Messi"}
pd.Series(diccionario)

print(diccionario)

PSG = {"Jugador":["Navas","Mbappe","Neymar","Messi"], "Altura":[183.00,170.00,170.00,165],"Goles":[2,3,4,10]}
DATA= pd.DataFrame(PSG,index=[1,7,10,30])
print(DATA)
