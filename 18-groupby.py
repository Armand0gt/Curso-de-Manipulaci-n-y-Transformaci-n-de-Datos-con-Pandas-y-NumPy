import pandas as pd
#Cargar archivo CSV
DataCSV = pd.read_csv("E:/VISUAL STUDE/PANDAS Y NUMPY/PUNTOS 01.csv",sep=";",header=0) 

print(DataCSV)
Filas = DataCSV.head(2)
print(Filas)

#agrupar
agrupar = DataCSV.groupby("DESCRIPCION").count()
agrupar = DataCSV.groupby("DESCRIPCION").mean()
agrupar = DataCSV.groupby("DESCRIPCION").max()
agrupar = DataCSV.groupby("DESCRIPCION").min()
agrupar = DataCSV.groupby("DESCRIPCION").median()
agrupar = DataCSV.groupby("DESCRIPCION").sum()
print(agrupar)

#para saber el minimo y el maximo
minmax = DataCSV.groupby("ESTE").agg("min", "max")
print(minmax)

#para saber el minimo y el maximo, suma 
minmax = DataCSV.groupby("DESCRIPCION").agg({"NORTE":["min", "max"],"ESTE":"sum"})
print(minmax)

#Organizar
organizar = DataCSV.groupby(["DESCRIPCION","NORTE"]).count()
print(organizar)
