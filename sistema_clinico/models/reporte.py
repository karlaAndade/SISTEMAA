# models/reporte.py

from datetime import date

class Reporte:
    def __init__(self, paciente, medico):
        self.__paciente = paciente
        self.__medico = medico
        self.__resultados = []
        self.__fecha_emision = date.today()
        self.__firmado = False

    def agregar_resultado(self, resultado):
        """
        Agrega un resultado al reporte.
        """
        self.__resultados.append(resultado)

    def mostrar_resumen(self) -> str:
        resumen = f"Reporte de {self.__paciente._nombre} {self.__paciente._apellido}\n"
        resumen += f"Emitido por Dr. {self.__medico._nombre} {self.__medico._apellido}\n"
        resumen += f"Fecha: {self.__fecha_emision}\n\nResultados:\n"
        for res in self.__resultados:
            resumen += f" - {res.mostrar_detalle()}\n"
        return resumen

    def marcar_como_firmado(self, medico):
        """
        Marca el reporte como firmado si el médico coincide.
        """
        if medico == self.__medico:
            self.__firmado = True

    def esta_firmado(self) -> bool:
        return self.__firmado
