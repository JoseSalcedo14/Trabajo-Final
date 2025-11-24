import pandas as pd
from datetime import datetime

class Ruta():
    def __init__(self, id, tarifa):
        self.__id = id
        self.__tarifa = tarifa
        self.__cantidad = 0

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def tarifa(self):
        return self.__tarifa
    @tarifa.setter
    def tarifa(self, tarifa):
        self.__tarifa = tarifa
        
    @property
    def cantidad(self):
        return self.__cantidad
    
    def __str__(self):
        return f"ID de la ruta: {self.__id} -> tarifa mensual: S/ {self.__tarifa}."


class Vehiculo():
    def __init__(self, placa, capacidad):
        self.__placa = placa
        self.__capacidad = capacidad
        self.__uso = False
    
    @property
    def placa(self):
        return self.__placa
    @placa.setter
    def placa(self, placa):
        self.__placa = placa
        
    @property
    def capacidad(self):
        return self.__capacidad
    @capacidad.setter
    def capacidad(self, capacidad):
        self.__capacidad = capacidad
        
    @property
    def uso(self):
        return self.__uso
    
    def __str__(self):
        return f"Placa: {self.__placa} -> capacidad del vehículo: {self.__capacidad} personas."


def validar_fecha(fecha_str, formato="%d/%m/%Y"):
    try:
        datetime.strptime(fecha_str, formato)
        return True
    except ValueError:
        return False
 
 
def volver():  
    while True:
        valido = input("\nIngrese 'S' para volver al menú principal > ").strip().upper()

        if valido == "S":
            return
        else:
            print("Ingrese un valor válido.\n")

 
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
    
    
def validar_placa(placa_vehiculo):
    placa_vehiculo = placa_vehiculo.upper()
    if len(placa_vehiculo) != 7:
        return False
    
    if not placa_vehiculo[:3].isalpha():
        return False
    
    if placa_vehiculo[3] != "-":
        return False
    
    if not placa_vehiculo[4:].isdigit():
        return False
    
    return True


def r_vehiculo():
    # Validación
    try:
        vehiculos = pd.read_csv("Datos/Vehiculos.csv", sep=";")
    except FileNotFoundError:
        print("\nNo existe el archivo 'Vehiculos'.\n")
        return
        
    a = "\nRegistro de vehículos"
    print(a)
    print("-" * len(a))
    
    while True:
        try:
            placa = input("\nIngrese la placa del vehículo > ").upper().strip()
            
            if not validar_placa(placa):
                print("Placa del vehiculo inválida.\n")
                continue
            
            if placa in vehiculos['Placa'].values:
                print("Ya hay un vehículo con esa placa.")
                continue
            break
        except ValueError:
            print("Ingrese un valor válido.")

    # Se solicita la capacidad del vehículo.
    while True:
        try:
            capacidad = int(input("Ingrese la capacidad del vehículo > "))

            # Se valida que la capacidad sea mayor o igual a 1.
            if capacidad < 1:
                print("La capacidad no puede ser menor a 1.")
                continue
            break
        except ValueError:
            print("Ingrese un valor válido.")

    vehiculo = Vehiculo(placa, capacidad)
    print("\nRuta creada con éxito.")
    print(vehiculo)
    
    # Agregando los datos al CSV
    n_vehiculo = pd.DataFrame([{
        'Placa':placa, 
        'Capacidad':capacidad, 
        'En_uso':0
        }])
    n_vehiculo.to_csv("Datos/Vehiculos.csv", sep=";", index=False, mode="a", header=False)
    volver()
    
    
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
                case 2:
                    r_vehiculo()
                case other:
                    print("Saliendo del programa...")
                    break
        except ValueError:
            print("Opción inválida")
    
main()