import numpy as np
array = np.random.randint(10, size = 20)
array[array <5] = 0
print(array)
media= np.mean(array)
print(f"Media del array: {media}")
mayores = array[array>media]
print(mayores)