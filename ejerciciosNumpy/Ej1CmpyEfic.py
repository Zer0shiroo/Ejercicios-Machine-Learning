import numpy as np
import sys
import time
n =999999
lista_py=list(range(n))
n= 0
inicios = time.time()
for i in lista_py:
    n += i
finals = time.time()
totaltiempos = finals - inicios
print(f"Tiempo usando buclefor: {totaltiempos}")
inicio = time.time()  
suma = np.sum(range(999999))
fin = time.time()
tiempo_transcurrido = fin - inicio
print(f"Tiempo usando np.sum:{tiempo_transcurrido}")
print(f"Memoria buclefor: {sys.getsizeof(n) } bytes")
print(f"Memoria np.sum: {suma.nbytes} bytes")