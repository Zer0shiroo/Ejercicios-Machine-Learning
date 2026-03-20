frase = input("Introduce una frase: ")

palabras = frase.split()

palabras_invertidas = []

for palabra in palabras:
    invertida = palabra[::-1]
    palabras_invertidas.append(invertida)

resultado = " ".join(palabras_invertidas)

print("Frase invertida:", resultado)