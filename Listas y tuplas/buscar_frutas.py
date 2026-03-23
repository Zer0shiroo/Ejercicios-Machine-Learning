tupla = ("platano", "pera", "manzana", "uvas")
intento = input("Dime una fruta")
intento = intento.lower()
comprobacion = False
for fruta in tupla:
    if intento == fruta:
        comprobacion = True
        print("Acertaste")
if comprobacion == False:
    print("Fallaste")