import pandas as pd
#Cargar archivo CSV
DataCSV = pd.read_csv("E:/VISUAL STUDE/PANDAS Y NUMPY/PUNTOS 01.csv",sep=";",header=0) 

print(DataCSV)
Filas = DataCSV.head(2)
print(Filas)

#Mayor que
Mayor = DataCSV["ELEVACION"] > 3176
print(Mayor)

Datamayor = DataCSV[Mayor]
print(Datamayor)

#O tambien se puede utilizar el mayor que de esta forma
Mayor = DataCSV[DataCSV["ELEVACION"] > 3176]
print(Mayor)

Descripcion = DataCSV["DESCRIPCION"] == "R"
print(Descripcion)
Dosculm = DataCSV(Descripcion & Mayor)
print(Dosculm)

