# models/medico.py

from models.persona import Persona

class Medico(Persona):
    def __init__(self, nombre: str, apellido: str, cedula: str, telefono: str,
                 codigo_medico: str, especialidad: str):
        super().__init__(nombre, apellido, cedula, telefono)
        self.__codigo_medico = codigo_medico
        self.__especialidad = especialidad
        
    def mostrar_info(self) -> str:
        return (
            f"Médico: {self._nombre} {self._apellido}\n"
            f"Cédula: {self._cedula}, Teléfono: {self._telefono}\n"
            f"Especialidad: {self._especialidad}, Código: {self._codigo_medico}"
    )

    def firmar_reporte(self, reporte):
        """
        Firma un reporte (se supone que 'reporte' es una instancia de la clase Reporte).
        """
        reporte.marcar_como_firmado(self)
