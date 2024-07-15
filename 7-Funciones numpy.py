import numpy as np

array = np.random.randint(1,20,10)
print(array)

matriz = array.reshape(2,5)
print(matriz)

max = array.max()
print(max)

matriz = matriz.max(0)
print(matriz)

max = array.argmax()
print(max)


min = array.min()
print(min)

matriz = matriz.min(0)
print(matriz)

min = array.argmin()
print(min)

percentil = np.percentile(array,25)
print(percentil)

#Desviacionestandar
desvestandar = np.std(array)**2
print(desvestandar)

#Varianza
varianza = np.var(array)
print(varianza)

#Media
media = np.mean(array)
print(media)

#Concatenar
a = np.array([1,2], [3,4])
b = np.array([5,6])

concatenar = np.concatenate([a,b],axis=0)