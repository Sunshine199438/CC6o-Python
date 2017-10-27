import numpy as np

m = [[5,4,7],[0,3,4],[0,0,6]]
a = np.array([[5,4,7],[0,3,4],[0,0,6]])

print (a)
print (a.traspose())

print (a[1, :])
print (a[1][1])
print (a[-1][-1])

print (a.mean())
print (a.diagonal())
print (a.ndim)
print (type(m))
print (type(a))
