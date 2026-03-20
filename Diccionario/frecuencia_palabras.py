texto = input("Dime una frase")
palabras = texto.split()
frecuencia = {}
for palabra in palabras:
     if palabra in frecuencia:
        frecuencia[palabra] = frecuencia[palabra] + 1
     else:
        frecuencia[palabra] = 1
print("Frecuencia de palabras:")
for palabra in frecuencia:
    print(f"{palabra}: {frecuencia[palabra]}")