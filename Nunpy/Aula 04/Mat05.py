import numpy as np

#lista Python
l = [20, 30, 10, 40]
#converter lista para array
a = np.array(l)

#print (l)
#print (a)
b = a[:]
c = a.copy()
c[1] = 999
a[1] = 1000
print (a)
print (b)
print (c)
#print(type(a))
#print(type(b))

#print(a[1])
#print(b[1])

#b[1] = 789
#print (a)
#print (b)
#print(a[1])
#print(b[1])
