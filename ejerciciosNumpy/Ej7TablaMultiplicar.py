import numpy as np
fila   = np.array([1, 2, 3, 4, 5])          
columna = np.array([1, 2, 3, 4, 5])         

fila    = fila.reshape(1, 5)                  
columna = columna.reshape(5, 1)              

matriz = columna * fila                       
print(matriz)