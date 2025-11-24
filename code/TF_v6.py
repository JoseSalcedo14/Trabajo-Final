from abc import ABC, abstractmethod
from datetime import datetime
import pandas as pd
import os


class Persona(ABC):
    def __init__(self, nombres, apellidos, dni):
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__dni = dni

    @property
    def nombres(self):
        return self.__nombres
    @nombres.setter
    def nombres(self, nva_nombres):
        self.__nombres = nva_nombres

    @property
    def apellidos(self):
        return self.__apellidos
    @apellidos.setter
    def apellidos(self, nva_apellidos):
        self.__apellidos = nva_apellidos

    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self, nva_dni):
        self.__dni = nva_dni

    @abstractmethod
    def mostrar_inf(self):
        pass


class Ruta:
    def __init__(self, id, tarifa, cant_alumnos):
        self.__id = id
        self.__tarifa = tarifa
        self.__cant_alumnos = cant_alumnos

    @property
    def id(self):
        return self.__id
    @id.setter
    def id_ruta(self, nueva_id):
        self.__id = nueva_id

    @property
    def tarifa(self):
        return self.__tarifa
    @tarifa.setter
    def tarifa_mens(self, nva_tarifa):
        self.__tarifa = nva_tarifa

    @property
    def cant_alumnos(self):
        return self.__cant_alumnos
    @cant_alumnos.setter
    def cant_alumnos(self, n_cant_alumnos):
        self.__cant_alumnos = n_cant_alumnos
    
    def __str__(self):
        return (
            f"* ID: {self.__id}\n"
            f"* Tarifa mensual: {self.__tarifa:.2f}\n"
            f"* Cantidad de alumnos: {self.__cant_alumnos}"
        )
        
       
class Vehiculo:
    def __init__(self, placa, cap_veh, en_uso):
        self.__placa = placa
        self.__cap_veh = cap_veh
        self.__en_uso = en_uso

    @property
    def placa(self):
        return self.__placa
    @placa.setter
    def placa(self, nva_placa):
        self.__placa = nva_placa

    @property
    def cap_veh(self):
        return self.__cap_veh
    @cap_veh.setter
    def cap_veh(self, nva_cap_veh):
        self.__cap_veh = nva_cap_veh

    @property
    def en_uso(self):
        return self.__en_uso
    @en_uso.setter
    def en_uso(self, valor):
        self.__en_uso = valor
        
    def __str__(self):
        return (
            f"* Placa: {self.__placa}\n"
            f"* Capacidad: {self.__cap_veh}\n"
            f"* ¿Está en uso?: {self.__en_uso}"
        )
        
        
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
    @brevete.setter
    def brevete(self, nva_brevete):
        self.__brevete = nva_brevete

    @property
    def cad_brevete(self):
        return self.__cad_brevete
    @cad_brevete.setter
    def cad_brevete(self, n_cad_brevete):
        self.__cad_brevete = n_cad_brevete

    @property
    def vehiculo(self):
        return self.__vehiculo
    @vehiculo.setter
    def vehiculo(self, nva_vehiculo):
        self.__vehiculo = nva_vehiculo

    @property
    def brevete(self):
        return self.__brevete
    @brevete.setter
    def brevete(self, n_brevete):
        self.__brevete = n_brevete

    @property
    def rutas(self):
        return self.__rutas
    @rutas.setter
    def rutas(self, rutas):
        self.__rutas = rutas
    
    def mostrar_inf(self):
        print(f"* Nombres: {self.nombres}")
        print(f"* Apellidos: {self.apellidos}")
        print(f"* DNI: {self.dni}")
        print(f"* Brevete: {self.__brevete}")
        print(f"* Fecha de caducidad del brevete: {self.__cad_brevete}")
        print(f"* Vehículo: {self.__vehiculo}")
        print("* Rutas:")
        for ruta in self.__rutas:
            print(f"  - {ruta}")


class Estudiante(Persona):
    def __init__(self, nombres, apellidos, dni, ruta_asignada):
        super().__init__(nombres, apellidos, dni)
        self.__ruta_asignada = ruta_asignada

    @property
    def ruta_asignada(self):
        return self.__ruta_asignada
    @ruta_asignada.setter
    def ruta_asignada(self, ruta_asignada):
        self.__ruta_asignada = ruta_asignada

    def mostrar_inf(self):
        print(f"* Nombres: {self.nombres}")
        print(f"* Apellidos: {self.apellidos}")
        print(f"* DNI: {self.dni}")
        print(f"* Ruta asignada: {self.__ruta_asignada}")


# Funciones de validaciones generales 
def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%d-%m-%y")
        return True
    except ValueError:
        return False


def validar_cad(fecha_str, formato="%d-%m-%y"):
    try:
        fecha = datetime.strptime(fecha_str, formato)
        fecha_actual = datetime.now()
        return not fecha.date() < fecha_actual.date()
    except ValueError:
        return False
    
    
def validar_dni(dni):
    try:
        dni = int(dni)
        return len(str(dni)) == 8
    except ValueError:
        return False
    
    
def validar_placa(placa_vehiculo):    
    if(
        len(placa_vehiculo) != 7
        or not placa_vehiculo[:3].isalpha()
        or placa_vehiculo[3] != "-"
        or not placa_vehiculo[4:].isdigit()
    ): return False
    return True


def validar_brevete(brevete):
    letra = brevete[0]
    numeros = brevete[1:]
    if(
        len(brevete) == 8
        and letra.isalpha()
        and letra.isupper() 
        and numeros.isdigit()
    ): return True
    
    return False


def validar_tarifa(tarifa):
    try:
        return float(tarifa) > 0
    except ValueError:
        return False


def validar_cantidad(cant):
    try:
        return int(cant) > 0
    except ValueError:
        return False


# Funciones principales
def crear_ruta():
    print("\nCREACIÓN DE RUTA")

    # Asegurase de que el archivo exista.
    nombre_archivo = "datos/rutas.csv"
    if not os.path.exists(nombre_archivo):
        rutas = pd.DataFrame(columns=["id_ruta", "tarifa", "cant_alumnos"])
        rutas.to_csv(nombre_archivo, sep=";", index=False)
        
    # Cargar los archivos existentes.
    rutas = pd.read_csv(nombre_archivo, sep=";")

    id_ruta = f"R{len(rutas) + 1:03d}"

    # Tarifa mensual
    while True:
        tarifa = input("Ingrese la tarifa mensual: ").strip()
        if not validar_tarifa(tarifa):
            print("Error: tarifa inválida. Debe ser un número mayor a 0.\n")
            continue
        break

    # La cantidad de alumnos inicia en cero.
    cant_alumnos = 0

    # Se crea el objeto 
    ruta = Ruta(id_ruta, float(tarifa), cant_alumnos)
    # Se guardan los datos
    nueva_ruta = pd.DataFrame([{
        "id_ruta": ruta.id,
        "tarifa": ruta.tarifa,
        "cant_alumnos": ruta.cant_alumnos,
    }])
    nueva_ruta.to_csv("datos/rutas.csv", sep=";", index=False, mode="a", header=False)
    
    print(f"Ruta {ruta.id} creada con éxito.\n")
    input("Presiona Enter para volver al menú principal")

    
def r_vehiculo():
    print("\nREGISTRO DE VEHÍCULO")
    # Asegurarse que el archivo exista.
    nombre_archivo = "datos/vehiculos.csv"
    if not os.path.exists(nombre_archivo):
        vehiculos = pd.DataFrame(columns=["placa_veh", "cap_veh", "en_uso"])
        vehiculos.to_csv(nombre_archivo, sep=";", index=False) 
    # Cargar los archivos existentes.
    vehiculos = pd.read_csv(nombre_archivo, sep=";")

    # Placa del vehículo
    while True:
        placa = input("Ingrese placa del vehículo (ejemplo: ABC-123): ").upper().strip()
        # Validar formato de la placa.
        if not validar_placa(placa):
            print("Error: placa inválida. Formato esperado: ABC-123.")
            continue
        break

    # Capacidad del vehículo.
    while True:
        cap_veh = int(input("Ingrese capacidad del vehículo: "))
        if not validar_cantidad(cap_veh-19):
            print("Error: capacidad inválida. Debe ser un número entero mayor o igual a 20.")
            continue
        break
    
    # Cuando se registra un vehículo este no está en uso. Por lo tanto, la variable se inicializa en False
    en_uso = False
    
    # Se crea el objeto
    vehiculo = Vehiculo(placa, cap_veh, en_uso)
    # Se guardan los datos
    n_vehiculo = pd.DataFrame([{
        'placa':vehiculo.placa, 
        'cap_veh':vehiculo.cap_veh, 
        'en_uso':vehiculo.en_uso
    }])
    n_vehiculo.to_csv("datos/vehiculos.csv", sep=";", index=False, mode="a", header=False)
    
    print(f"Vehículo {placa} registrado con éxito.")
    input("Presiona Enter para volver al menú principal")


def r_conductor():
    print("\nREGISTRO DE CONDUCTOR")

    nombre_archivo = "datos/conductores.csv"
    if not os.path.exists(nombre_archivo):
        conductores = pd.DataFrame(columns=[
            "dni", "nombres", "apellidos", "brevete" , "cad_brevete" ,"vehiculo", "rutas"
        ])
        conductores.to_csv(nombre_archivo, sep=";", index=False) 
    
    # Cargar los archivos existentes.
    conductores = pd.read_csv(nombre_archivo, sep=";")

    # Validar que existan rutas registradas
    try:
        rutas = pd.read_csv("datos/Rutas.csv", sep=';')
        if rutas.empty:
            print("No hay rutas registradas.\n")
            return
    except FileNotFoundError:
        print("\nNo existe el archivo 'Rutas'.\n")
        return
    
    # Validar que existan vehículos registrados y desocupados
    try:
        vehiculos = pd.read_csv("datos/vehiculos.csv", sep=";")
        if vehiculos.empty:
            print("No hay vehiculos registrados.\n")
            return
        
        if not any(vehiculos['en_uso'] == False):
            print("\nTodos los vehículos registrados estan en uso.")
            return
    except FileNotFoundError:
        print("\nNo existe el archivo 'Vehiculos'.\n")
        return
    
    # DNI del conductor
    while True:
        dni_conduc = input("Ingrese DNI del conductor > ")
        
        if not validar_dni(dni_conduc):
            print("Ingrese un DNI válido.\n")
            continue
        # Se valida que el DNI no esté registrado.
        if int(dni_conduc) in conductores['dni'].values:
            print("El conductor ya está registrado.")
            continue
        break
  
    # Nombres
    while True:
        nombres = input("Ingrese nombre de su personaje > ").title().strip()
        
        if nombres.isdigit():
            print("Error: ingreso inválido.\n")
            continue
        if not nombres:
            print("Error: ingreso inválido.\n")
            continue
        break
    
    # Apellidos
    while True:
        apellidos = input("Ingrese apellido de su personaje > ").title().strip()
    
        if apellidos.isdigit():
            print("Error: ingreso inválido.\n")
            continue
        if not apellidos:
            print("Error: ingreso inválido.\n")
            continue
        break
    
    # Se solicita el código de su brevete.
    while True:
        brevete = input("Ingrese brevete del conductor (EJ: A1234567) > ").strip().upper()
        
        if not validar_brevete(brevete):
            print("Debe ingresar un brevete válido.")
            continue
        break
    
    # Se solicita la fecha de caducidad del brevete.
    while True:
        caducidad = input("Ingrese la fecha de caducidad del brevete (dd-mm-aa) > ").strip()
        if not validar_cad(caducidad):
            print("Fecha inválida o brevete caducido.\n")
            continue
        break


    # Se asigna un vehículo disponible al conductor.
    while True:
        vehiculo = input("Ingrese la placa de su vehículo > ").strip().upper()
            
        if not validar_placa(vehiculo):
            print("Placa del vehiculo inválida.\n")
            continue
        # Se valida que el vehículo exista en el diccionario vehiculos.
        if vehiculo not in vehiculos['placa'].values:
            print("No hay un vehículo con esa placa.")
            continue
        # Se verifica el estado de uso del vehículo.
        if vehiculos.loc[vehiculos['placa'] == vehiculo, 'en_uso'].item():
            print("El vehículo ya está en uso.")
            continue
        break
    
    # Se solicita la cantidad de rutas asignadas
    while True:
        try:
            cantidad = int(input("¿Cuantas rutas tendrá el conductor? (Máximo 5) > "))
            if cantidad < 1 or cantidad > 5:
                print("Ingrese un valor válido.\n")
                continue
            break
        except ValueError:
            print("Ingrese un valor válido.\n")
    
    # Se buscan todos los objetos de clase Ruta
    l_rutas = []
    for enc, r in rutas.iterrows():
        l_rutas.append(Ruta(r['id_ruta'], r['tarifa'], r['cant_alumnos']))
    
    # Se solicitan las rutas asignadas.
    i = 1
    rutas_c = []
    while i <= cantidad:
        try:
            ruta = int(input(f"Ingrese la ruta {i} del conductor > "))

            # Se valida que la ruta exista.
            if ruta > len(l_rutas):
                print("No existe la ruta.\n")
                continue
            
            # Se valida que la ruta no esté asignada al conductor.
            if ruta in rutas_c:
                print("El conductor ya está asignado a esa ruta.")
                continue
    
            rutas_c.append(l_rutas[ruta-1].id)
            i += 1
        except ValueError:
            print("Ingrese un valor válido.")
    
    # Se crea el objeto
    conductor = Conductor(nombres, apellidos, int(dni_conduc), brevete, caducidad, vehiculo, rutas_c)
    
    # Cambiando el estado de uso del vehiculo asignado
    vehiculos.loc[vehiculos['placa'] == vehiculo, 'en_uso'] = True
    vehiculos.to_csv('datos/vehiculos.csv', sep=';', index=False)
    
    # Se guardan los datos
    nuevo_conduc = pd.DataFrame([{
        'dni':conductor.dni, 
        'nombres':conductor.nombres,
        'apellidos':conductor.apellidos, 
        'brevete':conductor.brevete,
        'cad_brevete': conductor.cad_brevete,
        'vehiculo': conductor.vehiculo,
        'rutas': ','.join(conductor.rutas)
        }])
    nuevo_conduc.to_csv("datos/conductores.csv", sep=";", index=False, mode="a", header=False)
    
    print("\nConductor registrado con éxito.")
    conductor.mostrar_inf()
    input("Presiona Enter para volver al menú principal")


def r_estudiante():
    print("\nREGISTRO DE ESTUDIANTE")

    # Asegurase de que el archivo exista.
    nombre_archivo = "datos/estudiantes.csv"
    if not os.path.exists(nombre_archivo):
        estudiantes = pd.DataFrame(columns=["id_ruta", "tarifa", "cant_alumnos"])
        estudiantes.to_csv(nombre_archivo, sep=";", index=False)
    
    # Cargar los datos existentes.
    estudiantes = pd.read_csv(nombre_archivo, sep=";")
    
    # Validar que existan rutas registradas
    try:
        rutas = pd.read_csv("datos/rutas.csv", sep=';')
        if rutas.empty:
            print("No hay rutas registradas.\n")
            return
    except FileNotFoundError:
        print("\nNo existe el archivo 'rutas'.\n")
        return
    
    # Se solicita el DNI
    while True:
        try:
            dni_est = input("\nIngrese DNI del estudiante > ")

            if not validar_dni(dni_est):
                print("Ingrese un DNI válido.\n")
                continue
            # Se valida que el DNI no esté ya registrado.
            if int(dni_est) in estudiantes['dni'].values:
                print("El estudiante ya está registrado.")
                continue
            break
        except ValueError:
            print("Ingrese un valor válido.")
            
    # Nombres
    while True:
        nombres = input("Ingrese nombre de su personaje > ").title().strip()
        
        if nombres.isdigit():
            print("Error: ingreso inválido.\n")
            continue
        if not nombres:
            print("Error: ingreso inválido.\n")
            continue
        break
    
    # Apellidos
    while True:
        apellidos = input("Ingrese apellido de su personaje > ").title().strip()
    
        if apellidos.isdigit():
            print("Error: ingreso inválido.\n")
            continue
        if not apellidos:
            print("Error: ingreso inválido.\n")
            continue
        break
    
    # Se buscan los objetos clase Ruta
    l_rutas = []
    for enc, r in rutas.iterrows():
        l_rutas.append(Ruta(r['id_ruta'], r['tarifa'], r['cant_alumnos']))
    
    # Se solicita la ruta asignada
    while True:
        try:
            ruta = int(input("Ingrese la ruta del estudiante > "))

            if ruta > len(l_rutas):
                print("La ruta no existe.")
                continue
            # Se valida que la ruta exista en el sistema.
            ruta_asignada = l_rutas[ruta-1].id
            break
        except ValueError:
            print("Ingrese un valor válido.")
    
    # Se crea el objeto 
    estudiante = Estudiante(nombres, apellidos, dni_est, ruta_asignada)
    
    # Agrengado 1 a la cantidad de alumnos en la ruta asignada
    rutas.loc[rutas['id_ruta'] == estudiante.ruta_asignada, 'cant_alumnos'] += 1
    rutas.to_csv('datos/rutas.csv', sep=';', index=False)
    
    # Se guardan los datos
    nuevo_est = pd.DataFrame([{
        'dni':estudiante.dni, 
        'nombres':estudiante.nombres,
        'apellidos':estudiante.apellidos, 
        'ruta':estudiante.ruta_asignada
        }])
    nuevo_est.to_csv("datos/estudiantes.csv", sep=";", index=False, mode="a", header=False)
    
    print("\nEstudiante registrado con éxito.")
    estudiante.mostrar_inf()
    input("Presiona Enter para volver al menú principal")


def mostrar_menu():
    a = "\nSistema de gestión de transporte escolar"
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


if __name__ == "__main__":
    main()