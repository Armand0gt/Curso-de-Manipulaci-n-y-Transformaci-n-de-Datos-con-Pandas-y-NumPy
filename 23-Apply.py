import pandas as pd
#Cargar archivo CSV
DataCSV = pd.read_csv("E:/VISUAL STUDE/PANDAS Y NUMPY/PUNTOS 01.csv",sep=";",header=0)

def two_time(Value):
    return Value*2

Imprimir = DataCSV["CURVAS"] = DataCSV["DESCRIPCION"].apply(two_time)
print(Imprimir)

CONDICION = DataCSV.apply(lambda X : X ["NORTE"]*2 if X ["ESTE"] == "BUZ" else X["NORTE"], axis=1)
print(CONDICION)