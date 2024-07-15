import numpy as np

list=list(range(0,10))
list1=np.arange(0,20,2)
print(list)
print(list1)

array= np.zeros([10,5])
print(array)

array1= np.zeros([10,5])
print(array1)

array1= np.ones([20,20])
print(array1)

lista2 =np.linspace(0,10,100)
print(lista2)


matriz3 = np.eye(4)
print(matriz3)

#Valores aleatorios
Valeatorio = np.random.rand()
print(Valeatorio)
Valeatorio1 = np.random.rand(5)
print(Valeatorio1)

#Valores enteros
venteros= np.random.randint(0,100,(10,10))
print(venteros)