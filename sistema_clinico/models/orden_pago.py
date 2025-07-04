# models/orden_pago.py

class OrdenPago:
    def __init__(self, paciente):
        self.__paciente = paciente
        self.__examenes = []

    def agregar_examen(self, examen):
        self.__examenes.append(examen)

    def calcular_total(self) -> float:
        return sum(examen.obtener_precio() for examen in self.__examenes)

    def mostrar_detalle(self) -> str:
        detalle = f"Orden de Pago - Paciente: {self.__paciente._nombre} {self.__paciente._apellido}\n"
        for examen in self.__examenes:
            detalle += f" - {examen.obtener_nombre()}: ${examen.obtener_precio():.2f}\n"
        detalle += f"Total: ${self.calcular_total():.2f}"
        return detalle
