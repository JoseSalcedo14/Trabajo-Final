from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import pandas as pd


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
        for ruta in self.__rutas.split(","):
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
def validar_arch():
    datos = {}

    # Rutas
    try:
        rutas = pd.read_csv("datos/rutas.csv", sep=';')
        if not rutas.empty:
            datos["rutas"] = True
        else:
            datos["rutas"] = False
    except FileNotFoundError:
        rutas = pd.DataFrame(columns=["id_ruta", "tarifa", "cant_alumnos"])
        rutas.to_csv("datos/rutas.csv", sep=";", index=False)
        datos["rutas"] = False

    # Vehiculos
    try:
        vehiculos = pd.read_csv("datos/vehiculos.csv", sep=';')
        if not vehiculos.empty:
            datos["vehiculos"] = True
        else:
            datos["vehiculos"] = False
    except FileNotFoundError:
        vehiculos = pd.DataFrame(columns=["placa", "cap_veh", "en_uso"])
        vehiculos.to_csv("datos/vehiculos.csv", sep=";", index=False)
        datos["vehiculos"] = False

    # Conductores
    try:
        conductores = pd.read_csv("datos/conductores.csv", sep=';')
        if not conductores.empty:
            datos["conductores"] = True
        else:
            datos["conductores"] = False
    except FileNotFoundError:
        conductores = pd.DataFrame(
            columns=[
                "dni", "nombres", "apellidos",
                "brevete", "cad_brevete",
                "vehiculo", "rutas",
            ]
        )
        conductores.to_csv("datos/conductores.csv", sep=";", index=False)
        datos["conductores"] = False

    # Estudiantes
    try:
        estudiantes = pd.read_csv("datos/estudiantes.csv", sep=';')
        if not estudiantes.empty:
            datos["estudiantes"] = True
        else:
            datos["estudiantes"] = False
    except FileNotFoundError:
        estudiantes = pd.DataFrame(columns=["dni", "nombres", "apellidos", "ruta"])
        estudiantes.to_csv("datos/estudiantes.csv", sep=";", index=False)
        datos["estudiantes"] = False

    # Asistencias
    try:
        asistencias = pd.read_csv("datos/asistencias.csv", sep=';')
        if not asistencias.empty:
            datos["asistencias"] = True
        else:
            datos["asistencias"] = False
    except FileNotFoundError:
        asistencias = pd.DataFrame(columns=["dni", "nombres", "apellidos", "placa"])
        asistencias.to_csv("datos/asistencias.csv", sep=";", index=False)
        datos["asistencias"] = False

    return datos


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


def validar_asis(fecha_str, formato="%d-%m-%y"):
    try:
        fecha = datetime.strptime(fecha_str, formato)
        fecha_actual = datetime.now()
        f_min = fecha_actual - timedelta(days=10)
        if f_min <= fecha <= fecha_actual:
            return True
        else:
            return False
    except ValueError:
        return False


def validar_dni(dni):
    try:
        int(dni)
        return len(str(dni)) == 8
    except ValueError:
        return False


def validar_texto(texto):
    if texto.isdigit():
        return False
    if not texto:
        return False
    return True


def validar_placa(placa_vehiculo):
    try:
        if (
            len(placa_vehiculo) != 7
            or not placa_vehiculo[:3].isalpha()
            or placa_vehiculo[3] != "-"
            or not placa_vehiculo[4:].isdigit()
        ):
            return False
        return True
    except ValueError:
        return False


def validar_brevete(brevete):
    letra = brevete[0]
    numeros = brevete[1:]
    if len(brevete) == 8 and letra.isalpha() and letra.isupper() and numeros.isdigit():
        return True

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


def crear_ruta():
    print("\nCREACIÓN DE RUTA")

    nombre_archivo = "datos/rutas.csv"  # Archivo principal.    
    # Cargar los archivos existentes.
    rutas = pd.read_csv(nombre_archivo, sep=";")

    # Se asigna una ID automática de acuerdo al número de ruta que se está registrando.
    id_ruta = f"R{len(rutas) + 1:03d}"

    # Tarifa mensual.
    while True:
        tarifa = input("Ingrese la tarifa mensual: ").strip()
        if not validar_tarifa(tarifa):
            print("Error: tarifa inválida. Debe ser un número mayor a 0.\n")
            continue
        break

    # La cantidad de alumnos inicia en cero.
    cant_alumnos = 0

    # Se crea el objeto.
    ruta = Ruta(id_ruta, float(tarifa), cant_alumnos)

    # Se guardan los datos.
    nueva_ruta = pd.DataFrame(
        [
            {
                "id_ruta": ruta.id,
                "tarifa": ruta.tarifa,
                "cant_alumnos": ruta.cant_alumnos,
            }
        ]
    )
    nueva_ruta.to_csv(nombre_archivo, sep=";", index=False, mode="a", header=False)
    print(f"Ruta {ruta.id} creada con éxito.")
    print("\nDATOS DE LA RUTA REGISTRADA")
    print(ruta)
    input("\nPresione 'Enter' para volver al menú principal.")


def r_vehiculo():
    print("\nREGISTRAR VEHÍCULO")

    nombre_archivo = "datos/vehiculos.csv"  # Arch principal
    # Cargar los archivos existentes.
    vehiculos = pd.read_csv(nombre_archivo, sep=";")

    # Placa del vehículo.
    while True:
        placa = input("Ingrese placa del vehículo (ejemplo: ABC-123): ").upper().strip()
        if placa in vehiculos["placa"].values:
            print("El vehículo ya está registrado.\n")
            continue

        # Validar formato de la placa.
        if not validar_placa(placa):
            print("Error: placa inválida. Formato esperado: ABC-123.")
            continue
        break

    # Capacidad del vehículo.
    while True:
        cap_veh = int(input("Ingrese capacidad del vehículo (mínimo 20): "))
        if not validar_cantidad(cap_veh - 19):
            print(
                "Error: capacidad inválida. Debe ser un número entero mayor o igual a 20."
            )
            continue
        break

    # Al registrar un vehículo, este no estará en uso. Por lo tanto, la variable se inicializa en False.
    en_uso = False

    # Se crea el objeto.
    vehiculo = Vehiculo(placa, int(cap_veh), en_uso)

    # Se guardan los datos.
    n_vehiculo = pd.DataFrame(
        [
            {
                "placa": vehiculo.placa,
                "cap_veh": vehiculo.cap_veh,
                "en_uso": vehiculo.en_uso,
            }
        ]
    )
    n_vehiculo.to_csv(nombre_archivo, sep=";", index=False, mode="a", header=False)
    print(f"Vehículo '{placa}' registrado con éxito.")
    print("\nDATOS DEL VEHÍCULO REGISTRADO")
    print(vehiculo)
    input("\nPresione 'Enter' para volver al menú principal.")


def r_conductor():
    print("\nREGISTRAR CONDUCTOR")

    nombre_archivo = "datos/conductores.csv"  # Archivo principal
    # Cargar los archivos existentes.
    conductores = pd.read_csv(nombre_archivo, sep=";")
    rutas = pd.read_csv("datos/rutas.csv", sep=";")
    vehiculos = pd.read_csv("datos/vehiculos.csv", sep=";")

    # Validar que existan vehículos desocupados.
    if not any(vehiculos["en_uso"] == False):
        print("Todos los vehículos registrados estan en uso.\n")
        return

    # DNI del conductor
    while True:
        dni_conduc = input("Ingrese DNI del conductor: ")
        if not validar_dni(dni_conduc):
            print("Error: ingrese un DNI válido.\n")
            continue

        # Se valida que el DNI no esté registrado.
        if int(dni_conduc) in conductores["dni"].values:
            print("El conductor ya está registrado.\n")
            continue
        break

    # Nombres.
    while True:
        nombres = input("Ingrese nombre(s) del conductor: ").title().strip()
        if not validar_texto(nombres):
            print("Error: Ingreso inválido.\n")
            continue
        break

    # Apellidos.
    while True:
        apellidos = input("Ingrese apellidos del conductor: ").title().strip()
        if not validar_texto(apellidos):
            print("Error: Ingreso inválido.\n")
            continue
        break

    # Se solicita el código de su brevete.
    while True:
        brevete = (
            input("Ingrese código del brevete (ejemplo: A1234567): ").strip().upper()
        )
        if not validar_brevete(brevete):
            print(
                "Error: debe ingresar un brevete válido. Formato esperado: A1234567.\n"
            )
            continue
        break

    # Se solicita la fecha de caducidad del brevete.
    while True:
        caducidad = input("Ingrese fecha de caducidad del brevete (dd-mm-aa): ").strip()
        if not validar_cad(caducidad):
            print("Error: fecha inválida o brevete caducido.\n")
            continue
        break

    # Se asigna un vehículo disponible al conductor.
    while True:
        vehiculo = (
            input("Ingrese placa del vehículo a asignar (ejemplo: ABC-123): ")
            .strip()
            .upper()
        )
        if not validar_placa(vehiculo):
            print("Error: placa inválida. Formato esperado: ABC-123.\n")
            continue

        # Se valida que el vehículo exista en el diccionario vehiculos.
        if vehiculo not in vehiculos["placa"].values:
            print("Error: no hay un vehículo con esa placa.\n")
            continue

        # Se verifica el estado de uso del vehículo.
        if vehiculos.loc[vehiculos["placa"] == vehiculo, "en_uso"].item():
            print("El vehículo ya está en uso.\n")
            continue
        break

    # Se buscan todos los objetos de clase 'Ruta'.
    l_rutas = []
    for enc, r in rutas.iterrows():
        l_rutas.append(Ruta(r["id_ruta"], r["tarifa"], r["cant_alumnos"]))

    # Se solicita la cantidad de rutas asignadas.
    while True:
        try:
            cantidad = int(input("¿Cuántas rutas tendrá el conductor? (máximo 5): "))
            if not 1 <= cantidad <= 5:
                print("Error: ingreso inválido.\n")
                continue
            if cantidad > len(l_rutas):
                print("Error: el valor ingresado supera las rutas disponibles.\n")
                continue
            break
        except ValueError:
            print("Error: ingreso inválido.\n")

    # Se solicitan las rutas asignadas.
    i = 1
    rutas_c = []
    while i <= cantidad:
        try:
            ruta = int(input(f"Ingrese la ruta {i} del conductor: "))

            # Se valida que la ruta exista.
            if ruta > len(l_rutas):
                print("Error: no existe la ruta.\n")
                continue

            # Se valida que la ruta no esté asignada al conductor.
            if ruta in rutas_c:
                print("El conductor ya está asignado a esa ruta.\n")
                continue

            rutas_c.append(l_rutas[ruta - 1].id)
            i += 1
        except ValueError:
            print("Error: ingreso inválido.\n")

    # Se crea el objeto.
    conductor = Conductor(
        nombres,
        apellidos,
        int(dni_conduc),
        brevete,
        caducidad,
        vehiculo,
        ",".join(rutas_c),
    )

    # Cambiando el estado de uso del vehiculo asignado.
    vehiculos.loc[vehiculos["placa"] == vehiculo, "en_uso"] = True
    vehiculos.to_csv("datos/vehiculos.csv", sep=";", index=False)

    # Se guardan los datos.
    nuevo_conduc = pd.DataFrame(
        [
            {
                "dni": conductor.dni,
                "nombres": conductor.nombres,
                "apellidos": conductor.apellidos,
                "brevete": conductor.brevete,
                "cad_brevete": conductor.cad_brevete,
                "vehiculo": conductor.vehiculo,
                "rutas": conductor.rutas,
            }
        ]
    )
    nuevo_conduc.to_csv(nombre_archivo, sep=";", index=False, mode="a", header=False)

    print(f"Conductor {nombres} registrado con éxito.")
    print("\nDATOS DEL CONDUCTOR REGISTRADO")
    conductor.mostrar_inf()
    input("\nPresione 'Enter' para volver al menú principal.")


def r_estudiante():
    print("\nREGISTRAR ESTUDIANTE")

    nombre_archivo = "datos/estudiantes.csv"  # Archivo principal
    # Cargar los datos existentes.
    estudiantes = pd.read_csv(nombre_archivo, sep=";")
    rutas = pd.read_csv("datos/rutas.csv", sep=";")

    # Se solicita el DNI.
    while True:
        dni_est = input("Ingrese DNI del estudiante (ejemplo: 12345678): ")
        if not validar_dni(dni_est):
            print("Error: DNI inválido. Formato esperado: 12345678.\n")
            continue

        # Se valida que el DNI ya esté registrado.
        dni_est = int(dni_est)
        if dni_est in estudiantes["dni"].values:
            print("El estudiante ya está registrado.\n")
            continue
        break

    # Nombres.
    while True:
        nombres = input("Ingrese nombre(s) del estudiante: ").title().strip()
        if not validar_texto(nombres):
            print("Error: Ingreso inválido.\n")
            continue
        break

    # Apellidos.
    while True:
        apellidos = input("Ingrese apellidos del estudiante: ").title().strip()
        if not validar_texto(apellidos):
            print("Error: Ingreso inválido.\n")
            continue
        break

    # Se buscan los objetos clase 'Ruta'.
    l_rutas = []
    for enc, r in rutas.iterrows():
        l_rutas.append(Ruta(r["id_ruta"], r["tarifa"], r["cant_alumnos"]))

    # Se solicita la ruta asignada.
    while True:
        try:
            ruta = int(input("Ingrese ruta del estudiante: "))
            if ruta > len(l_rutas):
                print("Error: no existe la ruta.\n")
                continue

            # Se valida que la ruta exista en el sistema.
            ruta_asignada = l_rutas[ruta - 1].id
            break
        except ValueError:
            print("Error: ingreso inválido.\n")

    # Se crea el objeto.
    estudiante = Estudiante(nombres, apellidos, dni_est, ruta_asignada)

    # Agregando 1 a la cantidad de alumnos en la ruta asignada.
    rutas.loc[rutas["id_ruta"] == estudiante.ruta_asignada, "cant_alumnos"] += 1
    rutas.to_csv("datos/rutas.csv", sep=";", index=False)

    # Se guardan los datos.
    nuevo_est = pd.DataFrame(
        [
            {
                "dni": estudiante.dni,
                "nombres": estudiante.nombres,
                "apellidos": estudiante.apellidos,
                "ruta": estudiante.ruta_asignada,
            }
        ]
    )
    nuevo_est.to_csv(nombre_archivo, sep=";", index=False, mode="a", header=False)

    print(f"Estudiante {nombres} registrado con éxito.")
    print("\nDATOS DEL ESTUDIANTE REGISTRADO")
    estudiante.mostrar_inf()
    input("\nPresione 'Enter' para volver al menú principal.")


def r_asistencia():
    nombre_archivo = "datos/asistencias.csv"  # Archivo principal
    # Cargar los archivos existentes.
    asistencias = pd.read_csv(nombre_archivo, sep=";")
    conductores = pd.read_csv("datos/conductores.csv", sep=";")
    estudiantes = pd.read_csv("datos/estudiantes.csv", sep=";")

    # Se solicita el DNI.
    while True:
        dni_est = input("Ingrese DNI del estudiante (ejemplo: 12345678): ")
        if not validar_dni(dni_est):
            print("Error: DNI inválido. Formato esperado: 12345678.\n")
            continue
        dni_est = int(dni_est)

        # Se valida que el DNI no esté ya registrado.
        if dni_est not in estudiantes["dni"].values:
            print("El estudiante no está registrado.\n")
            continue
        break

    # Se solicita la fecha.
    while True:
        fecha = input("Ingrese la fecha de asistencia (dd-mm-aa): ").strip()
        if not validar_asis(fecha):
            print("Error: fecha inválida.")
            print("Solo se pueden registrar asistencias de un máximo de 14 días anteriores.\n")
            continue
        break

    # Si el estudiante ya tiene la asistencia registrada en esa fecha, se retorna.
    existe_as = asistencias.loc[
        (asistencias["fecha"] == fecha) & (asistencias["dni"] == dni_est)
    ]
    if not existe_as.empty:
        print("La asistencia del estudiante ya fue registrada.")
        return

    ruta_est = estudiantes.loc[estudiantes["dni"] == dni_est, "ruta"].item()
    print(f"El estudiante está asignado a la ruta {ruta_est}.\n")

    # Se pide asistencia del estudiante.
    while True:
        presente = input("¿El estudiante estuvo presente? (S/N):").upper().strip()
        if presente == "S":
            presencia = True
        elif presente == "N":
            presencia = False
        else:
            print("Error: ingreso inválido.\n")
            continue
        break

    # Si el estudiante asistió, se solicita la placa del vehículo.
    if presencia:
        # Lista de todos los conductores registrados.
        l_conduc = []
        for enc, cond in conductores.iterrows():
            l_conduc.append(
                Conductor(
                    cond["dni"], cond["nombres"], cond["apellidos"],
                    cond["brevete"], cond["cad_brevete"],
                    cond["vehiculo"], cond["rutas"],
                )
            )

        # Vehículos que pasen por la ruta del estudiante.
        r_placas = []
        for cond in l_conduc:
            if ruta_est in cond.rutas.split(","):
                r_placas.append(cond.vehiculo)

        # Enumeración de las placas.
        for i, placa in enumerate(r_placas, 1):
            print(f"{i}. {placa}")

        while True:
            try:
                veh = int(input("¿En qué vehículo estaba el estudiante?: "))
                if not 1 <= veh <= len(r_placas):
                    print(f"Error: ingreso inválido.\n")
                    continue
                break
            except ValueError:
                print("Error: ingreso inválido.\n")
        veh_placa = r_placas[veh - 1]
    else:
        veh_placa = "None"

    # Se guardan los datos.
    n_asistencia = pd.DataFrame(
        [{"dni": dni_est, "fecha": fecha, "presente": presencia, "placa": veh_placa}]
    )
    n_asistencia.to_csv(nombre_archivo, sep=";", index=False, mode="a", header=False)

    if presencia:
        asist = "Asistió"
    else:
        asist = "No asistió"

    print("Asistencia registrada con éxito.")
    print("\nDATOS DE LA ASISTENCIA")
    print(f"DNI: {dni_est}")
    print(f"Fecha: {fecha}")
    print(f"¿Asistió?: {asist}")
    if presencia:
        print(f"Vehículo: {veh_placa}")
    input("\nPresione 'Enter' para volver al menú principal.")


def control_asis():
    archivos = validar_arch()
    while True:
        try:
            print("\nCONTROLAR ASISTENCIAS")
            print("1. Ver asistencias por fecha")
            print("2. Ver asistencias por estudiante")
            print("3. Ver asistencias por ruta")
            print("4. Volver al menú principal")
            opcion = int(input("Ingrese una opción: "))
            if not 1 <= opcion <= 4:
                print("Error: opción inválida.\n")
                continue
            break
        except ValueError:
            print("Error: opción inválida.\n")
    match opcion:
        case 1:
            filtro_fecha()
        case 2:
            filtro_est()
        case 3:
            if not archivos['estudiantes']:
                print("No hay estudiantes registrados.\n")
                return
            filtro_ruta()
        case 4:
            return


def filtro_fecha():
    print("\nVER ASISTENCIAS POR FECHA")
    asistencias = pd.read_csv("datos/asistencias.csv", sep=";")
    while True:
        fecha = input("Ingrese fecha de asistencia (dd-mm-aa): ").strip()
        if not validar_fecha(fecha):
            print("Error: fecha inválida.\n")
            continue
        if not fecha in asistencias["fecha"].values:
            print("No hay asistencias registradas en esa fecha.")
            continue
        break
    print()
    
    f_asis = asistencias[asistencias["fecha"] == fecha].rename(columns={
        "dni": "DNI",
        "fecha": "Fecha",
        "presente": "Presente",
        "placa": "Placa"
    })

    if f_asis.empty:
        print("No hay asistencias registradas en esa ruta.\n")
        return
    
    print(f_asis.to_string(index=False))

def filtro_est():
    print("\nVER ASISTENCIAS POR ESTUDIANTE")
    asistencias = pd.read_csv("datos/asistencias.csv", sep=";")
    while True:
        dni_est = input("Ingrese DNI del estudiante: ")
        if not validar_dni(dni_est):
            print("Error: DNI inválido.\n")
            continue
        if not dni_est in asistencias["dni"].values:
            print("No hay asistencias registradas de este DNI.\n")
            continue
        break

    print()
    f_asis = asistencias[asistencias["dni"] == dni_est].rename(columns={
        "dni": "DNI",
        "fecha": "Fecha",
        "presente": "Presente",
        "placa": "Placa"
    })

    if f_asis.empty:
        print("No hay asistencias registradas en esa ruta.\n")
        return
    
    print(f_asis.to_string(index=False))


def filtro_ruta():
    print("\nVER ASISTENCIAS POR RUTA")
    asistencias = pd.read_csv("datos/asistencias.csv", sep=";")
    estudiantes = pd.read_csv("datos/estudiantes.csv", sep=";")

    rutas = estudiantes["ruta"].unique().tolist()

    print("\rRutas disponibles:")
    for i, ruta in enumerate(rutas, 1):
        print(f"{i}. {ruta}")

    while True:
        try:
            opc = int(input("Seleccione una ruta: "))
            if 1 <= opc <= len(rutas):
                ruta_s = rutas[opc - 1]
                break
            else:
                print("Error: ingreso inválido.")
        except ValueError:
            print("Error: ingreso inválido")
    
    est_ruta = estudiantes[estudiantes["ruta"] == ruta_s]
    resultado = asistencias[asistencias["dni"].isin(est_ruta["dni"])]
    
    if resultado.empty:
        print("No hay asistencias registradas en esa ruta.\n")
        return

    f_asis = resultado.rename(columns={
        "dni": "DNI",
        "fecha": "Fecha",
        "presente": "Presente",
        "placa": "Placa"
    })
    print(f_asis.to_string(index=False))
    

def rutas_mu():
    pass


def menu_reportes():
    print("1. Rutas más usadas")
    print("2. Estudiante con mayor asistencia")
    print("3. Vehículos más usados")
    print("4. Conductores con más recorridos")
    print("5. Ingresos por ruta")
    print("6. Porcentaje de asistencia de un alumno.")
    print("7. Porcentaje de asistencias por rutas")
    print("8. Volver al menú principal")


def ver_reportes():
    while True:
        menu_reportes()
        try:
            opc = int(input("Ingrese una opción: "))
            if not 1 <= opc <= 8:
                print("Error: opción inválida.")
                continue
            break
        except ValueError:
            print("Error: opción inválida.")
    match opc:
        case 1:
            rutas_mu()
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            return


def opciones(opc):
    archivos = validar_arch()
    match opc:
        case 1:
            crear_ruta()
        case 2:
            r_vehiculo()
        case 3:
            if not archivos["rutas"] or not archivos["vehiculos"]:
                print("No hay rutas o vehículos registrados.\n")
                return
            r_conductor()
        case 4:
            if not archivos["rutas"]:
                print("No hay rutas registradas.\n")
                return
            r_estudiante()
        case 5:
            if not archivos["conductores"] or not archivos["estudiantes"]:
                print("No hay conductores o estudiantes registrados.\n")
                return
            r_asistencia()
        case 6:
            if not archivos["asistencias"]:
                print("No hay asistencias registradas.\n")
                return
            control_asis()
        case 7:
            ver_reportes()
        case 8:
            print("Saliendo del programa...")
            exit()
        case _:
            print("Error: opción inválida.")


def mostrar_menu():
    print()
    print("=" * 25)
    print(f"{'BUSERÍN':^25}")
    print("=" * 25)
    print("1. Crear rutas")
    print("2. Registrar vehículos")
    print("3. Registrar conductor")
    print("4. Registrar estudiante")
    print("5. Registrar asistencia")
    print("6. Control de asistencias")
    print("7. Ver reportes")
    print("8. Salir del programa")


def main():
    while True:
        mostrar_menu()
        # Rutas, Vehiculos, Conductores, Estudiantes, Asistencias
        archivos = validar_arch()
        try:
            opc = int(input("Ingrese una opción: "))
            if not 1 <= opc <= 8:
                print("Error: opción inválida.")
                continue
            opciones(opc)
        except ValueError:
            print("Error: opción inválida.")


if __name__ == "__main__":
    main()
