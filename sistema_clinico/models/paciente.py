# models/paciente.py

from datetime import date
from models.persona import Persona

class Paciente(Persona):
    def __init__(self, nombre: str, apellido: str, cedula: str, telefono: str,
                 fecha_nacimiento: date, sexo: str, direccion: str):
        super().__init__(nombre, apellido, cedula, telefono)
        self.__fecha_nacimiento = fecha_nacimiento
        self.__sexo = sexo
        self._direccion = direccion

    def obtener_edad(self) -> int:
        """
        Calcula la edad del paciente.
        """
        hoy = date.today()
        edad = hoy.year - self.__fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.__fecha_nacimiento.month, self.__fecha_nacimiento.day):
            edad -= 1
        return edad
    def mostrar_info(self) -> str:
        return (
            f"Paciente: {self._nombre} {self._apellido}\n"
            f"Cédula: {self._cedula}, Teléfono: {self._telefono}\n"
            f"Edad: {self.obtener_edad()}, Sexo: {self.__sexo}\n"
            f"Dirección: {self._direccion}"
    )
