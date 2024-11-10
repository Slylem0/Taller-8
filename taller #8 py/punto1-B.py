import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import tabulate

matrix = np.array([[2, -3, 4], [1, -2, 1], [3, 1, 2]])
resultados_matrix = np.array([-12, -5, 1])
matriz_aumentada = np.column_stack((matrix, resultados_matrix))

print(tabulate.tabulate(matriz_aumentada))

determinantes = np.linalg.solve(matrix, resultados_matrix)
print (determinantes)



