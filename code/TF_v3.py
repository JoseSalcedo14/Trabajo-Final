class Persona:
    def __init__(self, nombres, apellidos, dni):
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__dni = dni

    def get_nombres(self):
        return self.__nombres

    def set_nombres(self, nva_nombres):
        self.__nombres = nva_nombres

    def get_apellidos(self):
        return self.__apellidos

    def set_apellidos(self, nva_apellidos):
        self.__apellidos = nva_apellidos

    def get_dni(self):
        return self.__dni

    def set_dni(self, nva_dni):
        self.__dni = nva_dni

    def mostrar_inf(self):
        pass


class Conductor(Persona):
    def __init__(self, nombres, apellidos, dni, brevete, cad_brevete, vehiculo):
        super().__init__(nombres, apellidos, dni)
        self.__brevete = brevete
        self.__cad_brevete = cad_brevete
        self.__vehiculo = vehiculo
        self.__rutas = []

    def get_brevete(self):
        return self.__brevete

    def set_brevete(self, nva_brevete):
        self.__brevete = nva_brevete

    def get_cad_brevete(self):
        return self.__cad_brevete

    def set_cad_brevete(self, nva_cad_brevete):
        self.__cad_brevete = nva_cad_brevete

    def get_vehiculo(self):
        return self.__vehiculo

    def set_vehiculo(self, nva_vehiculo):
        self.__vehiculo = nva_vehiculo

    def agregar_ruta(self, ruta):
        if isinstance(ruta, Ruta):
            self.__rutas.append(ruta)
        else:
            print("Error: el objeto no es una instancia de la clase Ruta.")

    def mostrar_inf(self):
        print(f"Nombres: {self.get_nombres()}")
        print(f"Apellidos: {self.get_apellidos()}")
        print(f"DNI: {self.get_dni()}")
        print(f"Brevete: {self.__brevete}")
        print(f"Fecha de caducidad del brevete: {self.__cad_brevete}")
        print(f"Vehículo: {self.__vehiculo}")
        print(f"Rutas:")
        if not self.__rutas:
            print("No tiene rutas registradas.")
        else:
            for ruta in self.__rutas:
                print(f"- {ruta}")


class Ruta:
    def __init__(self, id_ruta, tarifa_mens, cant_alumnos):
        self.__id_ruta = id_ruta
        self.__tarifa_mens = tarifa_mens
        self.__cant_alumnos = cant_alumnos

    def get_id_ruta(self):
        return self.__id_ruta

    def set_id_ruta(self, nva_id_ruta):
        self.__id_ruta = nva_id_ruta

    def get_tarifa_mens(self):
        return self.__tarifa_mens

    def set_tarifa_mens(self, nva_tarifa_mens):
        self.__tarifa_mens = nva_tarifa_mens

    def get_cant_alumnos(self):
        return self.__cant_alumnos

    def set_cant_alumnos(self, nva_cant_alumnos):
        self.__cant_alumnos = nva_cant_alumnos


class Estudiante(Persona):
    def __init__(self, nombres, apellidos, dni, ruta_asignada):
        super().__init__(nombres, apellidos, dni)
        self.__ruta_asignada = ruta_asignada

    def get_ruta_asignada(self):
        return self.__ruta_asignada

    def set_ruta_asignada(self, nva_ruta_asignada):
        if isinstance(nva_ruta_asignada, Ruta):
            self.__ruta_asignada = nva_ruta_asignada
        else:
            print("Error: el objeto no es una instancia de la clase Ruta.")

    def mostrar_inf(self):
        print(f"Nombres: {self.get_nombres()}")
        print(f"Apellidos: {self.get_apellidos()}")
        print(f"DNI: {self.get_dni()}")
        print(f"Ruta asignada: {self.__ruta_asignada}")


class Vehiculo:
    def __init__(self, placa_veh, cap_veh):
        self.__placa_veh = placa_veh
        self.__cap_veh = cap_veh
        self.__en_uso = False

    def get_placa_veh(self):
        return self.__placa_veh

    def set_placa_veh(self, nva_placa_veh):
        self.__placa_veh = nva_placa_veh

    def get_cap_veh(self):
        return self.__cap_veh

    def set_cap_veh(self, nva_cap_veh):
        self.__cap_veh = nva_cap_veh

    def get_en_uso(self):
        return self.__en_uso

    def set_en_uso(self, valor):
        self.__en_uso = valor
