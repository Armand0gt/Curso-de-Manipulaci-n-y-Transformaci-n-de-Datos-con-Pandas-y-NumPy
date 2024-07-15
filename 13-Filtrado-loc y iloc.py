
import pandas as pd
#Cargar archivo CSV
DataCSV = pd.read_csv("E:/VISUAL STUDE/PANDAS Y NUMPY/PUNTOS 01.csv",sep=";",header=0) 
print(DataCSV)
#Filtrar por filas
Fila = DataCSV[0:4] #Solo extraer 4 filas
print(Fila)
#Filtrar por columnas
Columna = DataCSV[["PUNTO","NORTE"]] #Solo extraer las columnas
print(Columna)

#LCO
#Filtrar todas columnas y filas
ColmFil = DataCSV.loc[:] #Solo extraer las columnas
print(ColmFil)
#Filtrar alginas   filas
ColmFil2 = DataCSV.loc[3:10, ["PUNTO", "ELEVACION"]] #Solo extraer ALGUNAS  columnas Y FILAS USANDO LOC
print(ColmFil2)

#Realizar alguna multiplicacion o otro tipo de operacion
ColmFil2 = DataCSV.loc[:, ["PUNTO", "ELEVACION"]] *-1
print(ColmFil2)

#Cuando se esta buscando a una descripcion en particular
ColmFil2 = DataCSV.loc[:, ["PUNTO", "DESCRIPCION"]] == "R"
print(ColmFil2)

#con ILOC,  no es necesario escribir el nombre del encabezado o columna, LOC si necesita el nombre del encabezado
ColmFil4 = DataCSV.iloc[:]
print(ColmFil4)

ColmFil4 = DataCSV.iloc[:,0:2]
print(ColmFil4)

#Si quiero modificar un valor
ColmFil4 = DataCSV.iloc[1,3]*-1
print(ColmFil4)

ColmFil4 = DataCSV.iloc[:2,2:]
print(ColmFil4)