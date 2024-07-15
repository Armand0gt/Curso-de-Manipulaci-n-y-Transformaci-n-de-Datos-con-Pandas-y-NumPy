import pandas as pd
#Cargar archivo CSV
DataCSV = pd.read_csv("E:/VISUAL STUDE/PANDAS Y NUMPY/PUNTOS 01.csv",sep=";",header=0) 

print(DataCSV)
Filas = DataCSV.head(2)
print(Filas)

#Info indica que columnas tiene, el index, indica cuantos valores no son nulos, el tipo de dato
informacion = DataCSV.info()
print(informacion)

#Informacion estadistica de los datos
Estadistic = DataCSV.describe()
print(Estadistic)

#Muestra los ultimos dos registros
ulregistro = DataCSV.tail(2)
print(ulregistro)

#Indica caunta memoria estoy usando en mi data frame
memoria = DataCSV.memory_usage(deep=True)
print(memoria)

#Cuenta la cantidad de veces que existe una descripcion, un valor en general
contar = DataCSV["DESCRIPCION"].value_counts()
print(contar)

#Elimina duplicados
DataCSV.iloc(0)

Duplicados = pd.concat([DataCSV,DataCSV.iloc[0].to_frame().T])
print(Duplicados)

Duplicados1 = Duplicados.drop_duplicates(keep="last")
print(Duplicados1)

#Ordenar los datos

ordenar = DataCSV.sort_values("DESCRIPCION")
print(ordenar)

ordenar = DataCSV.sort_values("ESTE",ascending=False) #Ordena de mayor a menor
print(ordenar)








