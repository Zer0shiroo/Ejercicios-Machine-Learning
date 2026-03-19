diccionario = {"nombre": "Angel", "edad": 20}
print(diccionario.get("nombre"))
diccionario.get("apellido", "No disponible") 
diccionario.update({"apellido": "Perez"})
edad = diccionario.pop("edad") 
diccionario.popitem()
diccionario.clear() 
diccionario = {"nombre": "Angel", "edad": 20}
claves = diccionario.keys()
print(claves)
print(diccionario.values()) 
print(diccionario.items())
nuevo_diccionario = diccionario.copy()
print(nuevo_diccionario)