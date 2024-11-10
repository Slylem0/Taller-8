import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import tabulate


matrix = np.array([[1, 1, 1], [1, 1, -2], [1, 3, -2]])
resultados = np.array([30, 0, 20])

matrix_aumentada = np.column_stack((matrix, resultados))

print (tabulate.tabulate(matrix_aumentada))

results = np.linalg.solve(matrix, resultados)
print (resultados)