capitales = {"Espana": "Madrid", "Argentina" : "Buenos Aires", "Francia" : "Paris", "Italia" : "Roma"}
nuevacap = input("Dime un pais de la lista")
for pais in capitales: 
    if pais == nuevacap:
        print(capitales[pais])
