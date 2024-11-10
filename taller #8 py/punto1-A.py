import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import tabulate
# Definir la matriz de coeficientes y el vector de resultados
matrix = np.array([[3, 2, 1], [4, 2, 2], [1, -1, 1]])
resultados_matrix = np.array([2, 8, 4])

# Crear la matriz aumentada
matriz_aumentada = np.column_stack((matrix, resultados_matrix))

# Mostrar la matriz aumentada
print(tabulate.tabulate(matriz_aumentada))
print("__________soluciones______")

# Resolver el sistema de ecuaciones
x = np.linalg.solve(matrix, resultados_matrix)
print("X =", int(x[0]), "\nY =", int(x[1]), "\nZ =", int(x[2]))

# Crear la figura 3D
figura = plt.figure()
ax = figura.add_subplot(111, projection='3d')

# Crear un rango de valores para el parámetro t
t = np.linspace(-10, 10, 100)

# Graficar las líneas de intersección en el espacio 3D
# Línea de intersección entre ecuaciones 1 y 2
x1 = t
y1 = (2 - 3 * t) / 2
z1 = 2 - 3 * t - 2 * y1
ax.plot(x1, y1, z1, color='red', label="Intersección eq1 y eq2")

# Línea de intersección entre ecuaciones 1 y 3
x2 = t
y2 = (4 - t) / 3
z2 = 4 - x2 + y2
ax.plot(x2, y2, z2, color='blue', label="Intersección eq1 y eq3")

# Línea de intersección entre ecuaciones 2 y 3
x3 = t
y3 = (8 - 4 * t) / 5
z3 = 4 - x3 + y3
ax.plot(x3, y3, z3, color='green', label="Intersección eq2 y eq3")

# Configurar los ejes y mostrar la gráfica
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
plt.show()
