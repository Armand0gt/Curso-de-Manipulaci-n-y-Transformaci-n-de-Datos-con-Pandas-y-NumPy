#Unir dos archivos
#lefjoin: le da prioridad a la izquierda
#rightjoin: le da prioridad a la derecha

import pandas as pd
import numpy as np

#Marge y concat

# Creazione dei DataFrames
Diccionario1 = pd.DataFrame({"A":["A0","A1","A2","A3"],
                               "B":["B0", "B1","B2","B3"],
                "C":["C0","C1","C2","C3"],
                "D":["D0","D1","D2","D3"]})

Diccionario2 = pd.DataFrame({"A":["A4","A5","A6","A7"],
                               "B":["B4", "B5","B6","B7"],
                "C":["C4","C5","C6","C7"],
                "D":["D4","D5","D6","D7"]})

Concatenar = pd.concat([Diccionario1,Diccionario2],ignore_index=True)
print(Concatenar)

Concatenar = pd.concat([Diccionario1,Diccionario2],axis=1)
print(Concatenar)

#Conbinacion entre izquierda y derecha.merge nos permite realizar "joins" entre tablas. 

izquierda = pd.DataFrame({"Key":["K0","K1","K2","K3"],
          "A":["A0","A1","A2","A3"],
          "B":["B0", "B1","B2","B3"]})

print(izquierda)
Derecha = pd.DataFrame({"Key":["K0","K1","K2","K3"],
          "C":["C0","C1","C2","C3"],
          "D":["D0", "D1","D2","D3"]})

print(Derecha)

Unir = izquierda.merge(Derecha, on="Key")
print(Unir)


izquierda = pd.DataFrame({"Key":["K0","K1","K2","K3"],
          "A":["A0","A1","A2","A3"],
          "B":["B0", "B1","B2","B3"]})

print(izquierda)
Derecha = pd.DataFrame({"Key2":["K0","K1","K2","K3"],
          "C":["C0","C1","C2","C3"],
          "D":["D0", "D1","D2","D3"]})

print(Derecha)

Unir = izquierda.merge(Derecha,left_on="Key", right_on="Key2")
print(Unir)


izquierda = pd.DataFrame({"Key":["K0","K1","K2","K3"],
          "A":["A0","A1","A2","A3"],
          "B":["B0", "B1","B2","B3"]})

print(izquierda)
Derecha = pd.DataFrame({"Key2":["K0","K1","K2",np.nan],
          "C":["C0","C1","C2","C3"],
          "D":["D0", "D1","D2","D3"]})
print(Derecha)


Unir = izquierda.merge(Derecha,left_on="Key", right_on="Key2", how="right")
print(Unir)

#Utilizar Join----Index match

Izquierda1 = pd.DataFrame({"A":["A0","A1","A2"],
        "B":["B0", "B1","B2"]},
        index=["k0","k1","k2"])

print(Izquierda1)

Derecha1 = pd.DataFrame({"C":["C0","C1","C2"],
        "D":["D0", "D1","D2"]},
        index=["k0","k2","k3"])

print(Derecha1)

Join = Izquierda1.join(Derecha1, how="inner")
print(Join)