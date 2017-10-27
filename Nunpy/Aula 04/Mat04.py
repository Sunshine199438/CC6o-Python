import numpy as np

joao_pts = [20, 30, 40, 15]
pedro_pts = [100, 24, 48, 23]
maria_pts = [20, 30, 40, 15]
marcos_pts = [100, 24, 48, 23]

pontos = np.array ([joao_pts,pedro_pts,maria_pts,marcos_pts])

print (pontos)
print (type(pontos))

my_data = np.arange(0.20)
print (my_data)


m1 = np.reshape(my_date, (5,4))
print (m1)
