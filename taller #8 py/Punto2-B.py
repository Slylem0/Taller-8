import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tabulate

# Matriz de coeficientes y vector de resultados
matriz = np.array([
    [1, 1, 1],
    [1, 0, 0],
    [27, 28, 31]
])

resultados = np.array([540000, 162000, 15999000])

# Mostrar matriz aumentada
matriz_aumentada = np.column_stack((matriz, resultados))
print(tabulate.tabulate(matriz_aumentada, headers=["S1", "S2", "S3", "Resultados"]))

# Resolver el sistema de ecuaciones
try:
    soluciones = np.linalg.solve(matriz, resultados)
    print("\nSoluciones (cantidad de barriles de cada proveedor):", soluciones)
except np.linalg.LinAlgError:
    print("\nNo se puede resolver el sistema, posiblemente las ecuaciones no sean independientes.")

# Preparar la figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Rango para la variable libre
S3_vals = np.linspace(0, 540000, 100)

# Línea de intersección entre la ecuación 1 y 3
S2_vals_1 = 540000 - soluciones[0] - S3_vals
S1_vals_1 = (15999000 - 28 * S2_vals_1 - 31 * S3_vals) / 27

# Línea de intersección entre la ecuación 2 y 3 (S1 es constante en 162000)
S2_vals_2 = np.linspace(0, 540000, 100)
S1_vals_2 = 162000 * np.ones_like(S2_vals_2)
S3_vals_2 = (15999000 - 27 * S1_vals_2 - 28 * S2_vals_2) / 31

# Graficar las líneas
ax.plot(S2_vals_1, S3_vals, S1_vals_1, color='blue', label='Intersección Ecuación 1 y 3')
ax.plot(S2_vals_2, S3_vals_2, S1_vals_2, color='green', label='Intersección Ecuación 2 y 3')

# Etiquetas y título
ax.set_xlabel("S2 (Proveedor 2)")
ax.set_ylabel("S3 (Proveedor 3)")
ax.set_zlabel("S1 (Proveedor 1)")
ax.set_title("Intersección de ecuaciones de proveedores en 3D")
ax.legend()

plt.show()
