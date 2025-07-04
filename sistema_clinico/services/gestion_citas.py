# services/gestion_citas.py

from models.cita import Cita
from datetime import datetime

class ServicioCitas:
    def __init__(self):
        self.__citas = []

    def agendar_cita(self, paciente, medico, fecha_hora: datetime, motivo: str) -> Cita:
        nueva_cita = Cita(paciente, medico, fecha_hora, motivo)
        self.__citas.append(nueva_cita)
        return nueva_cita

    def listar_citas(self):
        return [cita.mostrar_detalle() for cita in self.__citas]
