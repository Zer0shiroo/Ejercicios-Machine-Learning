class Alumno:
    def __init__(self, nombre, nota_inicial):
        self.nombre = nombre
        self.lista_notas = [float(nota_inicial)]

    def registrar_nota(self):
        nueva_nota = float(input("Dime la nueva nota: "))
        self.lista_notas.append(nueva_nota)
        print("Nota insertada correctamente")

    def calcular_promedio(self):
        contador = 0
        total = 0
        for i in self.lista_notas:
            contador +=1
            total += i
        return total/contador

    def getnota(self):
        promedio = self.calcular_promedio()
        print(f"Notas: {self.lista_notas}")
        print(f"Promedio: {promedio}")
        print(f"Estado: {'Aprobado' if promedio >= 5 else 'Reprobado'}")