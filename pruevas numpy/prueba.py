import numpy as np
import sys

ventas = np.array([100, -50, 200, 0, 450, -10])

ventas_limpias = ventas[(ventas > 0) & (ventas < 400)]

print(ventas_limpias)