import pandas as pd
import numpy as pd
#Cargar archivo CSV
DataCSV = pd.read_csv("E:/VISUAL STUDE/PANDAS Y NUMPY/PUNTOS 01.csv",sep=";",header=0) 
print(DataCSV)

AFILAS = DataCSV.head(2) #Muestra las dos primeras filas y el encabezado
print(AFILAS)

#Eliminar columnas de un data frame
Eliminar = DataCSV.drop("DESCRIPCION", axis=1).head(2) #Solo lo elimina la columna de la pantalla
print(Eliminar)

Eliminar = DataCSV.drop("DESCRIPCION", axis=1, inplace=True) #Eliminar la columna permanentemente del archivo
print(Eliminar)
AFILAS = DataCSV.head(2) 
print(AFILAS)

Eliminar = DataCSV.drop("ELEVACION", axis=1) #Eliminar la columna permanentemente del archivo
print(Eliminar)
AFILAS = DataCSV.head(3) 
print(AFILAS)

#Borrar columnas
AFILAS = DataCSV.head(2) #Muestra las dos primeras filas y el encabezado
print(AFILAS)

Borrar = DataCSV.drop(0,axis = 0).head(2)
print(Borrar)

Borrar = DataCSV.drop([0,2,3],axis = 0).head(2) #Elimino algunas filas
print(Borrar)

Borrar = DataCSV.drop(range(0,10),axis = 0).head(2) #Elimino rango espeficicado filas
print(Borrar)

#Agregar columnas###No me func
#print(DataCSV.head(2))
#DataCSV["Nueva_columna"] = np.nan
#print(DataCSV)
