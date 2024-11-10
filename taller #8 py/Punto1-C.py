import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import tabulate


matrix = np.array([[2, 4, 6], [2, -3, -4], [3, 4, 5]])
resultados_matrix = np.array([-12, 15,-8])
matriz_aumentada = np.column_stack((matrix, resultados_matrix))

print(tabulate.tabulate(matriz_aumentada))

resultados = np.linalg.solve(matrix, resultados_matrix)
print (resultados)