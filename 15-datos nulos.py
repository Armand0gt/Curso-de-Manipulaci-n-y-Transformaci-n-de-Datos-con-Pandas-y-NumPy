import pandas as pd
import numpy as np

Diccionadior = {"Col1":[1,2,3,np.nan],
                "Col2":[4,np.nan,6,7], 
                "Col3":["a","b","c",None]}

data_frame   = pd.DataFrame(Diccionadior)
print(data_frame)

#Eliminar valores nulos
Nulo= data_frame.isnull()
print(Nulo)

Nulo= data_frame.isnull()*1
print(Nulo)
#Agregar un dato
llenar = data_frame.fillna("Mely")
print(llenar)


# El dato nulo colocarle la media
data_frame.fillna(data_frame.mean(numeric_only=True), inplace=True)  # Corregido
print(data_frame)  # Imprimir para ver los cambios

# Interpolar valores nulos
data_frame.interpolate(inplace=True)  # Corregido
print(data_frame)  # Imprimir para ver los cambios






