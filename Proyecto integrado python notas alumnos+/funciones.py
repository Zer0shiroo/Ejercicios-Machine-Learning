import Alumno 

registro_alumnos = {}

def registrar_alumno():
    nombre = input("Nombre del alumno: ")
    nota = float(input("Nota inicial: "))
    registro_alumnos[nombre] = Alumno.Alumno(nombre, nota)
    print(f"Alumno '{nombre}' registrado.")

def anadir_nota_alumno():
    if not registro_alumnos:
        print("No hay alumnos registrados aún.")
        return
    print("Alumnos:")
    for nombre in registro_alumnos:
        print(f"  - {nombre}")
    nombre = input("Nombre del alumno al que añadir nota: ")
    if nombre in registro_alumnos:
        registro_alumnos[nombre].registrar_nota()
    else:
        print("Alumno no encontrado.")

def reporte_alumno():
    if not registro_alumnos:
        print("No hay alumnos registrados aún.")
        return
    for nombre, alumno in registro_alumnos.items():
        print(f"\nAlumno: {nombre}")
        alumno.getnota()

def menu(sesion):
    print("\n------GESTION DE NOTAS DE ALUMNOS-----")
    print("1. Registrar nuevo alumno")
    print("2. Añadir nota a alumno existente")
    print("3. Reporte de cada alumno")
    print("4. Salir")
    print("--------------------------------------")

    opcion = int(input("Inserta numericamente la opcion requerida: "))

    if opcion == 1:
        registrar_alumno()
        return sesion
    elif opcion == 2:
        anadir_nota_alumno()
        return sesion
    elif opcion == 3:
        reporte_alumno()
        return sesion
    elif opcion == 4:
        print("Saliendo del programa")
        return False