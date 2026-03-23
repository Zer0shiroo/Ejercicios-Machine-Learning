nombre =  input("Dime tu nombre")
apellido = input("Dime tu apellido")
palabrasnombre = nombre.split()
palabrasapelido = apellido.split()
nombre = palabrasnombre[0][0]
apellido = palabrasapelido[0][0]
print(nombre.upper() + apellido.upper())