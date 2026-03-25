import numpy as np
# 3x + y  = 9
# x  + 2y = 8
A = np.array([[3, 1],
              [1, 2]])
b = np.array([9, 8])
solucion = np.linalg.solve(A, b)
print(f"x = {solucion[0]:.2f}")
print(f"y = {solucion[1]:.2f}")
