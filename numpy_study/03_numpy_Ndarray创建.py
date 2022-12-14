import numpy as np
data = np.array([1,2,3,4])
print(type(data))
print('------')
data1 = np.array((1,2,3,4,5))
print(type(data1))
print('------')
data2 = np.asarray([1,2,3,4])
print('------')
print(id(data))
print(id(data2))
print('------')
data3 = np.asarray(data)
print(data3)
print(id(data))
print(id(data3))
print('------')
data3[0] = 2
print(data)
print(data3)
print(id(data))
print(id(data3))
print('------')
data4 = np.arange(10)
print(data4)
print(type(data4))
print('------')
data5 = np.ones((5,), dtype=np.int8)
print(data5)
print('------')
data6 = np.ones_like(data5)
print(data6)
print('------')
data7 = np.eye(4)
print(data7)
print(data7.dtype)
print('------')
data8 = np.identity(4, dtype=np.int32)
print(data8)
print(data8.dtype)

