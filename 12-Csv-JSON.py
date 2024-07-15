#Instalar pip
#Importar pandas

import pandas as pd
#Cargar archivo CSV
DataCSV = pd.read_csv("E:/VISUAL STUDE/PANDAS Y NUMPY/PUNTOS 01.csv",sep=";",header=0) #Si mi archivo
# no es un Csv si no que esta delimitado por tabulaciones escribir despues del nombre del archivo,sep=(;)para este caso
# es coma, y no era necesario hacerlo.
# header=0 es el encabezado, si no tubiera encabezado el archivo solo escribir header=None
#name es para modificar las columnas, primero pasar el codigo que esta en la parte inferior y luego modificar
#las columnas si se desea
print(DataCSV)

#name es para modificar las columnas, primero pasar el codigo que esta en la parte inferior y luego modificar
#las columnas si se desea
Columnas = DataCSV.columns
print(Columnas)
MODIFCOLUM = pd.read_csv("E:/VISUAL STUDE/PANDAS Y NUMPY/PUNTOS 01.csv",sep=";",header=0,names=['PUNTO', 'X', 'Y', 'Z', 'D'])
print(MODIFCOLUM)

#Guardar como: archivo anterior
#DataCSV.to_csv("E:/VISUAL STUDE/PANDAS Y NUMPY/EJEMPLO 01.csv")

#Instalar en la terminal
#"""pip install openpyxl
#Importar el 
#Cargar archivo XLSX
#Dataxlsx = pd.read_excel("E:/VISUAL STUDE/PANDAS Y NUMPY/Ingredientes.xlsx", index_col=0,
 #                        engine="openpyxl")
#print(Dataxlsx)
#Guardar como: archivo anterior
#DataCSV.to_excel("E:/VISUAL STUDE/PANDAS Y NUMPY/IActivos.xlsx", sheet_name ="RONALDO", engine = "openpyxl")

