import numpy as np

lecturas = np.random.uniform(15, 35, size=24)
print("Lecturas originales:", lecturas)


turnos = lecturas.reshape(3, 8)
print("Matriz por turnos (3x8):", turnos)

max_por_turno = turnos.max(axis=1)   
print("Temperatura máxima por turno:", max_por_turno)

vector = turnos.ravel()           
print("Vector aplanado:", vector)
