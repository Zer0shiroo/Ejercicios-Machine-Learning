import numpy as np
matriz = np.random.randn(50, 4)
print("Matriz original:\n", matriz)
media = matriz.mean(axis=0)      
std   = matriz.std(axis=0)     
normalizada = (matriz - media) / std 

print("\nMedia de cada columna (debe ser ≈ 0):")
print(normalizada.mean(axis=0))

