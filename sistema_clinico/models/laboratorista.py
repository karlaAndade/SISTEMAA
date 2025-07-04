# models/laboratorista.py

from models.persona import Persona

class Laboratorista(Persona):
    def __init__(self, nombre: str, apellido: str, cedula: str, telefono: str,
                 codigo_laboratorista: str, turno: str):
        super().__init__(nombre, apellido, cedula, telefono)
        self.__codigo_laboratorista = codigo_laboratorista
        self.__turno = turno
    
    def mostrar_info(self) -> str:
        return (
            f"Laboratorista: {self._nombre} {self._apellido}\n"
            f"Cédula: {self._cedula}, Teléfono: {self._telefono}\n"
            f"Número de Registro: {self._numero_registro}"
    )

    def registrar_resultado(self, examen, valor):
        """
        Crea un resultado basado en un examen (instancia de Examen) y un valor numérico.
        """
        from models.resultado import Resultado
        return Resultado(examen, valor)
