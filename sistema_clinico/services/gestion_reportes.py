# services/gestion_reportes.py

from models.reporte import Reporte

class ServicioReportes:
    def __init__(self):
        self.__reportes = []

    def generar_reporte(self, paciente, medico) -> Reporte:
        nuevo_reporte = Reporte(paciente, medico)
        self.__reportes.append(nuevo_reporte)
        return nuevo_reporte

    def listar_reportes(self):
        return [reporte.mostrar_resumen() for reporte in self.__reportes]
