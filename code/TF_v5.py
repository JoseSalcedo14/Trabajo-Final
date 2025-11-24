import pandas as pd
from datetime import datetime

class Persona:
    def __init__(self, nombres, apellidos, dni):
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__dni = dni

    @property
    def nombres(self):
        return self.__nombres

    @property
    def apellidos(self):
        return self.__apellidos

    @property
    def dni(self):
        return self.__dni

    def mostrar_inf(self):
        pass


class Ruta:
    def __init__(self, id_ruta, tarifa_mens):
        self.__id_ruta = id_ruta
        self.tarifa_mens = tarifa_mens
        self.__cant_alumnos = 0

    @property
    def id_ruta(self):
        return self.__id_ruta

    @property
    def tarifa_mens(self):
        return self.__tarifa_mens
    @tarifa_mens.setter
    def tarifa_mens(self, tarifa_mens):
        if tarifa_mens <= 0:
            raise ValueError("La tarifa debe ser mayor a 0.\n")
        self.__tarifa_mens = tarifa_mens

    @property
    def cant_alumnos(self):
        return self.__cant_alumnos
    
    def __str__(self):
        return f"ID de la ruta: {self.__id_ruta} -> Tarifa mensual: {self.__tarifa_mens}."


class Vehiculo:
    def __init__(self, placa_veh, cap_veh):
        self.__placa_veh = placa_veh
        self.cap_veh = cap_veh
        self.__en_uso = False

    @property
    def placa_veh(self):
        return self.__placa_veh

    @property
    def cap_veh(self):
        return self.__cap_veh
    @cap_veh.setter
    def cap_veh(self, cap_veh):
        if cap_veh < 15:
            raise ValueError("El vehículo debe tener una capacidad mínima de 15 estudiantes.\n")
        self.__cap_veh = cap_veh

    @property
    def en_uso(self):
        return self.__en_uso
    
    def __str__(self):
        return f"Placa: {self.__placa_veh} -> capacidad del vehículo: {self.cap_veh} personas."


class Conductor(Persona):
    def __init__(self, nombres, apellidos, dni, brevete, cad_brevete, vehiculo, rutas):
        super().__init__(nombres, apellidos, dni)
        self.__brevete = brevete
        self.__cad_brevete = cad_brevete
        self.__vehiculo = vehiculo
        self.__rutas = rutas

    @property
    def brevete(self):
        return self.__brevete

    @property
    def cad_brevete(self):
        return self.__cad_brevete

    @property
    def vehiculo(self):
        return self.__vehiculo

    @property
    def rutas(self):
        return self.__rutas

    def mostrar_inf(self):
        print(f"Nombres: {self.nombres}")
        print(f"Apellidos: {self.apellidos}")
        print(f"DNI: {self.dni}")
        print(f"Brevete: {self.__brevete}")
        print(f"Fecha de caducidad del brevete: {self.__cad_brevete}")
        print(f"Vehículo: {self.__vehiculo}")
        print(f"Rutas:")
        if not self.__rutas:
            print("No tiene rutas registradas.")
        else:
            for ruta in self.__rutas:
                print(f"- {ruta}")


class Estudiante(Persona):
    def __init__(self, nombres, apellidos, dni, ruta_asignada):
        super().__init__(nombres, apellidos, dni)
        self.__ruta_asignada = ruta_asignada

    @property
    def ruta_asignada(self):
        return self.__ruta_asignada

    def mostrar_inf(self):
        print(f"Nombres: {self.nombres}")
        print(f"Apellidos: {self.apellidos}")
        print(f"DNI: {self.dni}")
        print(f"Ruta asignada: {self.__ruta_asignada}")


def validar_fecha(fecha_str, formato="%d/%m/%y"):
    try:
        fecha = datetime.strptime(fecha_str, formato)
        fecha_actual = datetime.now()
        if fecha.date() <= fecha_actual.date():
            return False
        return True
    except ValueError:
        return False
            

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


def volver():  
    while True:
        valido = input("\nIngrese 'S' para volver al menú principal > ").strip().upper()

        if valido == "S":
            return
        else:
            print("Ingrese un valor válido.\n")
            
            
def crear_ruta():
    # Validar que existe el archivo de rutas
    try:
        rutas = pd.read_csv("Datos/Rutas.csv", sep=";")
    except FileNotFoundError:
        print("\nNo existe el archivo 'Rutas'.\n")
        return
    
    a = "\nCreación de rutas"
    print(a)
    print("-" * len(a))
    
    # ID de la ruta
    id_ruta = len(rutas)+1
    
    # Tarifa mensual
    while True:
        try:
            tarifa = float(input("Ingrese tarifa mensual de la ruta: "))
            ruta = Ruta(id_ruta, tarifa)
            break
        except ValueError as e:
            print(e)
    print("\nRuta creada con éxito.")
    print(ruta)
    
    # Agregando los datos al CSV
    nueva_ruta = pd.DataFrame([{
        'ID_Ruta':ruta.id_ruta, 
        'Tarifa':ruta.tarifa_mens, 
        'Cantidad':0
        }])
    nueva_ruta.to_csv("Datos/Rutas.csv", sep=";", index=False, mode="a", header=False)
    volver()
    

def r_vehiculo():
    
    # Validar que exista el archivo de vehículos
    try:
        vehiculos = pd.read_csv("Datos/Vehiculos.csv", sep=";")
    except FileNotFoundError:
        print("\nNo existe el archivo 'Vehiculos'.\n")
        return
        
    a = "\nRegistro de vehículos"
    print(a)
    print("-" * len(a))
    
    while True:
        placa = input("\nIngrese la placa del vehículo > ").upper().strip()
            
        if not validar_placa(placa):
            print("Placa del vehiculo inválida.\n")
            continue
        if placa in vehiculos['Placa'].values:
            print("Ya hay un vehículo con esa placa.")
            continue
        break

    # Se solicita la capacidad del vehículo.
    while True:
        try:
            capacidad = int(input("Ingrese la capacidad del vehículo > "))
            vehiculo = Vehiculo(placa, capacidad)
            break
        except ValueError as e:
            print(e)
    print("\nRuta creada con éxito.")
    print(vehiculo)
        
    # Agregando los datos al CSV
    n_vehiculo = pd.DataFrame([{
        'Placa':vehiculo.placa_veh, 
        'Capacidad':vehiculo.cap_veh, 
        'En_uso':False
        }])
    n_vehiculo.to_csv("Datos/Vehiculos.csv", sep=";", index=False, mode="a", header=False)
    volver()


def r_conductor():
    
    # Validar que exista el archivo de conductores
    try:
        conductores = pd.read_csv("Datos/Conductores.csv", sep=';')
    except FileNotFoundError:
        print("\nNo existe el archivo 'Conductores'")
        return
    
    # Validar que existan rutas registradas
    try:
        rutas = pd.read_csv("Datos/Rutas.csv", sep=';')
        if rutas.empty:
            print("No hay rutas registradas.\n")
            return
    except FileNotFoundError:
        print("\nNo existe el archivo 'Rutas'.\n")
        return
       
    # Validar que existan vehículos registrados 
    try:
        vehiculos = pd.read_csv("Datos/Vehiculos.csv", sep=";")
        if vehiculos.empty:
            print("No hay vehiculos registrados.\n")
            return
    except FileNotFoundError:
        print("\nNo existe el archivo 'Vehiculos'.\n")
        return
    
    # Validar que al menos un vehículo no esté en uso
    if not any(vehiculos['En_uso'] == False):
        print("\nTodos los vehículos registrados estan en uso.")
        return
    
    while True:
        try:
            dni_conduc = int(input("\nIngrese DNI > "))

            # Se valida que el DNI tenga 8 dígitos.
            if len(str(dni_conduc)) != 8:
                print("El DNI debe tener 8 dígitos.")
                continue

            # Se valida que el DNI no esté registrado.
            if dni_conduc in conductores['DNI'].values:
                print("El conductor ya está registrado.")
                continue
            break
        except ValueError:
            print("Ingrese un valor válido.")
            
    nombres_conduc = input("Ingrese nombres del conductor > ").title().strip()
    apellidos_conduc = input("Ingrese apellidos del conductor > ").title().strip()
    
    # Se solicita el código de su brevete.
    while True:
        brevete = input("Ingrese brevete del conductor > ").strip().upper()

        # Se valida que el brevete tenga al menos 6 caracteres.
        if len(brevete) < 6:
            print("El brevete debe tener al menos 6 caracteres.")
            continue
        break
    
    # Se solicita la fecha de caducidad del brevete.
    while True:
        try:
            caducidad = input("Ingrese la fecha de caducidad del brevete (dd/mm/aa) > ").strip()
            if not validar_fecha(caducidad):
                print("Fecha inválida o brevete caducido.\n")
                continue
            break
        except ValueError:
            print("Ingrese un valor válido.")

    # Se asigna un vehículo disponible al conductor.
    while True:
        vehiculo = input("Ingrese la placa de su vehículo > ").strip().upper()
            
        if not validar_placa(vehiculo):
            print("Placa del vehiculo inválida.\n")
            continue
            
        # Se valida que el vehículo exista en el diccionario vehiculos.
        if vehiculo not in vehiculos['Placa'].values:
            print("No hay un vehículo con esa placa.")
            continue

            # Se verifica el estado de uso del vehículo.
        if vehiculos.loc[vehiculos['Placa'] == vehiculo, 'En_uso'].item():
            print("El vehículo ya está en uso.")
            continue
        break
            
    # Se inicializa la lista de rutas del conductor.
    rutas_c = []

    while True:
        try:
            cantidad = int(input("¿Cuantas rutas tendrá el conductor? (Máximo 5) > "))
            if cantidad < 1 or cantidad > 5:
                print("Ingrese un valor válido.\n")
                continue
            break
        except ValueError:
            print("Ingrese un valor válido.\n")
    
    # Se solicitan las rutas asignadas.
    i = 1
    while i <= cantidad:
        try:
            ruta = int(input(f"Ingrese la ruta {i} del conductor > "))

            # Se valida que la ruta exista.
            if ruta not in rutas['ID_Ruta'].values:
                print("La ruta no existe.")
                continue
            # Se valida que la ruta no esté asignada al conductor.
            elif ruta in rutas_c:
                print("El conductor ya está asignado a esa ruta.")
                continue
            
            rutas_c.append(ruta)
            i += 1
        except ValueError:
            print("Ingrese un valor válido.")
            
    conductor = Conductor(nombres_conduc, apellidos_conduc, dni_conduc, brevete, caducidad, vehiculo, rutas_c)
    print("\nConductor registrado con éxito.")
    conductor.mostrar_inf()
    
    # Cambiando el estado de uso del vehiculo asignado
    vehiculos.loc[vehiculos['Placa'] == vehiculo, 'En_uso'] = True
    vehiculos.to_csv('Datos/Vehiculos.csv', sep=';', index=False)
    
    nuevo_conduc = pd.DataFrame([{
        'DNI':conductor.dni, 
        'Nombres':conductor.nombres,
        'Apellidos':conductor.apellidos, 
        'Brevete':conductor.brevete,
        'Caducidad': conductor.cad_brevete,
        'Vehiculo': conductor.vehiculo,
        'Rutas':conductor.rutas
        }])
    nuevo_conduc.to_csv("Datos/Conductores.csv", sep=";", index=False, mode="a", header=False)
    volver()

def r_estudiante():
    
    # Validar que exista el archivo de estudiantes
    try:
        estudiantes = pd.read_csv("Datos/Estudiantes.csv", sep=';')
    except FileNotFoundError:
        print("\nNo existe el archivo 'Vehiculos'.\n")
        return
    
    # Validar que existan rutas registradas
    try:
        rutas = pd.read_csv("Datos/Rutas.csv", sep=';')
        if rutas.empty:
            print("No hay rutas registradas.\n")
            return
    except FileNotFoundError:
        print("\nNo existe el archivo 'Rutas'.\n")
        return
    
    a = "\nRegistro de estudiantes"
    print(a)
    print("-" * len(a))
    
    while True:
        try:
            dni_est = int(input("\nIngrese DNI del estudiante > "))

            # Se valida que el DNI tenga 8 dígitos.
            if len(str(dni_est)) != 8:
                print("El DNI debe tener 8 dígitos.")
                continue

            # Se valida que el DNI no esté ya registrado.
            if dni_est in estudiantes['DNI'].values:
                print("El estudiante ya está registrado.")
                continue
            break
        except ValueError:
            print("Ingrese un valor válido.")

    nombres = input("Ingrese los nombres del estudiante > ").title().strip()
    apellidos = input("Ingrese los apellidos del estudiante > ").title().strip()

    while True:
        try:
            ruta_asignada = int(input("Ingrese la ruta del estudiante > "))

            # Se valida que la ruta exista en el sistema.
            if ruta_asignada not in rutas['ID_Ruta'].values:
                print("La ruta no existe.")
                continue
            break
        except ValueError:
            print("Ingrese un valor válido.")
    
    estudiante = Estudiante(nombres, apellidos, dni_est, ruta_asignada)
    print("\nEstudiante registrado con éxito.")
    estudiante.mostrar_inf()
    
    # Agrengado 1 a la cantidad de alumnos en la ruta asignada
    rutas.loc[rutas['ID_Ruta'] == ruta_asignada, 'Cantidad'] += 1
    rutas.to_csv('Datos/Rutas.csv', sep=';', index=False)
    
    # Registrando el estudiante en el archivo CSV
    nuevo_est = pd.DataFrame([{
        'DNI':estudiante.dni, 
        'Nombres':estudiante.nombres,
        'Apellidos':estudiante.apellidos, 
        'Ruta':estudiante.ruta_asignada
        }])
    nuevo_est.to_csv("Datos/Estudiantes.csv", sep=";", index=False, mode="a", header=False)
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
                case 3:
                    r_conductor()
                case 4:
                    r_estudiante()
                case other:
                    print("Saliendo del programa...")
                    break
        except ValueError:
            print("Opción inválida")
main()