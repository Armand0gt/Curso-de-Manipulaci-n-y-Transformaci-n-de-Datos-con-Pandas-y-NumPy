import numpy as np

array = np.random.randint(1,10,(3,2))
print(array)

shape = (array.shape)
print(shape)

reshape = array.reshape(1,6)
print(reshape)

reshape = array.reshape(2,3)
print(reshape)

arr = np.reshape(array,(1,6))
print(arr)

arr = np.reshape(array,(2,3), "C")
print(arr)

arr = np.reshape(array,(2,3), "F")
print(arr)

arr = np.reshape(array,(2,3), "A")
print(arr)


