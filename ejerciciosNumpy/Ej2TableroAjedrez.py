import numpy as np
x = np.ones((8, 8))
x[::2, ::2] = 0
print(x)
