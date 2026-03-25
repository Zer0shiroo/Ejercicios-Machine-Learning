import numpy as np
requisitos_planeta = np.dtype([
    ('nombre', 'U10'), 
    ('diametro', 'f8'), 
    ('tiene anillos', '?')
])


planetas = np.array([
    ('Mercurio', 4879.4, False),
    ('Venus', 12104.0, False),
    ('Tierra', 12742.0, False),
    ('Marte', 6779.0, False),
    ('Jupiter', 139820.0, True),
    ('Saturno', 116460.0, True)
], dtype=requisitos_planeta)