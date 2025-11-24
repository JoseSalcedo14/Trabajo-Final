import pandas as pd
from datetime import datetime

class Ruta():
    def __init__(self, id:int, tarifa:float):
        self._id = id
        self._tarifa = tarifa
        self._cantidad = 0

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def tarifa(self):
        return self._tarifa
    @tarifa.setter
    def tarifa(self, tarifa):
        self._tarifa = tarifa
        
    @property
    def cantidad(self):
        return self._cantidad
    
    def __str__(self):
        return f"ID de la ruta: {self.id} -> tarifa mensual: S/ {self.tarifa}, cantidad de alumnos: {self.cantidad}."


def volver():  # No recibe parámetros.

    # Se solicita confirmación para volver al menú principal.
    while True:
        valido = input("\nIngrese 'S' para volver al menú principal > ").strip().upper()

        # Se valida que la entrada sea 'S'.
        if valido == "S":
            return
        else:
            print("Ingrese un valor válido.\n")
            
            
def mostrar_menu():
    a = "Sistema de gestión de transporte escolar"
    print(a)
    print("-" * len(a))
    print("1. Crear rutas")
    print("2. Registrar vehículos")
    print("3. Registrar conductor")
    print("4. Registrar estudiante")
    print("5. Registrar asistencia")
    print("6. Control de asistencia")
    print("7. Ver reportes")
    print("8. Salir")

            
def crear_ruta():
    # Validar que existe el archivo CSV
    try:
        rutas = pd.read_csv("Datos/Rutas.csv", sep=";")
    except FileNotFoundError:
        print("\nNo existe el archivo 'Rutas'.\n")
        return
    
    a = "\nCrear rutas"
    print(a)
    print("-" * len(a))
    
    # ID de la ruta
    id_ruta = len(rutas)+1
    
    # Tarifa mensual
    while True:
        try:
            tarifa = float(input("Ingrese tarifa mensual de la ruta: "))
            if tarifa < 0:
                print("La tarifa debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Tarifa mensual inválida.")
    
    ruta = Ruta(id_ruta, tarifa)
    print("\nRuta creada con éxito.")
    print(ruta)
    
    # Agregando los datos al CSV
    nueva_ruta = pd.DataFrame([{
        'ID_Ruta':id_ruta, 
        'Tarifa':tarifa, 
        'Cantidad':0
        }])
    nueva_ruta.to_csv("Datos/Rutas.csv", sep=";", index=False, mode="a", header=False)
    volver()

def main():
    while True:
        mostrar_menu()
        try:
            opc = int(input("Ingrese una opción > " ))
            if opc < 1 or opc > 8:
                print("Opción inválida.")
                continue
            match opc:
                case 1:
                    crear_ruta()
                case other:
                    print("Saliendo del programa...")
                    break
        except ValueError:
            print("Opción inválida")
main()