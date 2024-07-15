import numpy as np
arr = np.arange(0,11)
print(arr)
trozo_de_array = arr[0:6]
print(trozo_de_array)

trozo_de_array = arr[:] = 0
print(trozo_de_array)

arr_copy = arr.copy()
print(arr_copy)
