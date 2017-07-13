import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print (type(x))
print (x.shape)
print (x.dtype)

# the array can be indexed using python container like syntax
print (x[1, 2])
y = x[:, 1]
print (y)
# this also changes the corresonding element in x
y[0] = 9
print (y)
print (x)

a = np.ndarray(shape=(2,2), dtype=float, order='F')
print (a)

b = np.ndarray((2,), buffer=np.array([1,2,3]),
    offset=np.int_().itemsize,
    dtype=int) # offset = 1*itemsize, i.e. skip first element
print (b)
