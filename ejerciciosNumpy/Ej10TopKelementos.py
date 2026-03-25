import numpy as np
matriz = np.zeros((10, 10), dtype=float)
matriz[2:6, 2:6] = 1
print("Matriz original:\n", matriz.astype(int))
kernel = np.array([[ 0, -1,  0],
                   [-1,  4, -1],
                   [ 0, -1,  0]])
resultado = np.zeros_like(matriz)
for i in range(1, matriz.shape[0] - 1):
    for j in range(1, matriz.shape[1] - 1):
        region = matriz[i-1:i+2, j-1:j+2]  
        resultado[i, j] = np.sum(region * kernel)
print("Resultado tras convolución:", resultado.astype(int))
