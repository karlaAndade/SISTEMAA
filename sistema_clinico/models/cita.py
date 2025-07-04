# models/cita.py

from datetime import datetime

class Cita:
    def __init__(self, paciente, medico, fecha_hora: datetime, motivo: str):
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__motivo = motivo
        self.__atendida = False

    def marcar_como_atendida(self):
        self.__atendida = True

    def esta_atendida(self) -> bool:
        return self.__atendida

    def mostrar_detalle(self) -> str:
        estado = "Atendida" if self.__atendida else "Pendiente"
        return (f"Cita para {self.__paciente._nombre} con el Dr. {self.__medico._apellido}\n"
                f"el {self.__fecha_hora.strftime('%d/%m/%Y %H:%M')} - Motivo: {self.__motivo} - Estado: {estado}")
